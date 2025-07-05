sudo k8s kubectl -n kaniko create secret docker-registry srinidocker \
  --docker-server="https://index.docker.io/v1/" \
  --docker-username=NNNNNN \
  --docker-password="XXXXXX" \
  --docker-email=ksrinimba@gmail.com
