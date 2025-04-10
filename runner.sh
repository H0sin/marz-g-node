#!/bin/sh
docker stop marz-g-node
docker rm marz-g-node
docker build -t marz-g-node .

docker run \
  --name marz-g-node \
  --user root \
  -e IP_ADDRESS=167.235.20.19 \
  -p 50051:50051 \
  -v /certs/:/usr/src/marz-g-node/certs \
  -v /etc/rc.local:/etc/rc.local \
  --restart always \
  --privileged \
  --cap-add NET_ADMIN \
  --cap-add NET_RAW \
  marz-g-node
