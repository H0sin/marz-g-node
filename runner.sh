#!/bin/sh
#docker run -v /certs/:/usr/src/marz-g-node/certs -p 50051:50051 marz-g-node
docker run --network host -v /certs/:/usr/src/marz-g-node/certs marz-g-node