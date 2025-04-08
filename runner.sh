#!/bin/sh
docker stop marz-g-node
docker build -t marz-g-node .
docker run -v /certs/:/usr/src/marz-g-node/certs -p 50051:50051 --name marz-g-node marz-g-node
#docker run --network hos  -v /certs/:/usr/src/marz-g-node/certs marz-g-node
