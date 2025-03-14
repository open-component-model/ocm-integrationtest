#! /bin/sh
docker run -d --rm -p 4430:4430 -v "$(pwd)/certs:/certs" --name registry -e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm" -e REGISTRY_AUTH=htpasswd -e REGISTRY_AUTH_HTPASSWD_PATH=/certs/htpasswd -e REGISTRY_HTTP_ADDR=:4430 -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/ociregistry.crt -e REGISTRY_HTTP_TLS_KEY=/certs/ociregistry.key -e REGISTRY_STORAGE_DELETE_ENABLED=true registry:2.8.1
