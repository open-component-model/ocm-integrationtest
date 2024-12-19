# Module with helper classes for component-descriptors
from dataclasses import dataclass

import gci.componentmodel as cm
import gci.oci
import oci.auth as oa
import oci.client as oc
import yaml

import ocmcli as ocm


@dataclass(frozen=True)
class ComponentVersion:
    name: str
    version: str

    @staticmethod
    def from_component_descriptor(cd: cm.ComponentDescriptor):
        return ComponentVersion(name=cd.component.name, version=cd.component.version)


class OciFetcher:

    def __init__(self, repo_url: str, user_name: str = None, password: str = None):
        self.repo_url = repo_url
        self.user_name = user_name
        self.password = password

        self.ctx_repo = cm.OciRepositoryContext(baseUrl=repo_url)

        routes = oc.OciRoutes(self._base_api_lookup)
        self.client = oc.Client(
            credentials_lookup=self._credentials_lookup,
            routes=routes,
            disable_tls_validation=True,
        )


    def get_component_descriptor_from_registry(
        self,
        component_name: str,
        component_version: str,
        as_yaml: bool = False,
    ) -> cm.ComponentDescriptor | str:
        cd = ocm.execute_ocm(f'get component {self.ctx_repo.baseUrl}//{component_name}:{component_version} -oyaml')

        # Find the marker and process the content after it
        out = cd.stdout.decode("utf-8")
        marker = '---'
        if marker in out:
            processed_content = out.split(marker, 1)[1].strip()
        else:
            processed_content = ""

        docs = yaml.load_all(processed_content, yaml.SafeLoader)
        for doc in docs:
            if len(doc) == 0 or not doc['meta']:
                continue
            if doc is None:
                raise ValueError('Component Descriptor appears to be empty')
            print(f'Found component descriptor: {doc}')
            if as_yaml:
                return doc
            return gci.componentmodel.ComponentDescriptor.from_dict(doc)


    def get_component_descriptors_from_registry(
        self,
        component_name: str,
        component_version: str,
    ) -> dict[ComponentVersion, cm.ComponentDescriptor]:
        components = {}
        cd = self.get_component_descriptor_from_registry(
            component_name,
            component_version,
        )
        cv = ComponentVersion.from_component_descriptor(cd)
        components[cv] = cd
        for ref in cd.component.componentReferences:
            ref_cv = ComponentVersion(name=ref.componentName, version=ref.version)
            if not ref_cv in components:
                recursive_references = self.get_component_descriptors_from_registry(
                    component_name=ref_cv.name,
                    component_version=ref_cv.version,
                )
                components |= recursive_references # merge result dict
        return components


    def exists(self, image_reference: str) -> bool:
        blob_ref = self.client.head_manifest(image_reference, absent_ok = True)
        return blob_ref is not None


    @staticmethod
    def _base_api_lookup(image_reference):
        return oc.base_api_url(image_reference)


    @staticmethod
    def _normalise_component_name(component_name:str) -> str:
        return component_name.lower()  # oci-spec allows only lowercase


    def _credentials_lookup(
        self,
        image_reference: str,
        privileges: oa.Privileges=oa.Privileges.READONLY,
        absent_ok: bool=True,
    ):
        if self.password and self.user_name:
            return oa.OciBasicAuthCredentials(
                    username=self.user_name,
                    password=self.password,
                )
        else:
            return None
