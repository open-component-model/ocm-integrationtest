#! /bin/sh
# Linux:  FQDN_HOST=`hostname --fqdn`
# Macos:  ip=`ipconfig getifaddr en0` or check output of `scutil --dns`
#         FQDN_HOST=`dig -x $ip +short | head -c-2`
# manual: export FQDN_HOST=`hostname`.fritz.box
mkdir -p certs
openssl req -newkey rsa:4096 -nodes -sha256 -keyout certs/ociregistry.key -addext "subjectAltName = DNS:${FQDN_HOST}" -x509 -days 365 -out certs/ociregistry.crt -subj "/C=DE/ST=Baden-Wuertemberg/L=Walldorf/O=SAP/OU=ocm/CN=${FQDN_HOST}"
