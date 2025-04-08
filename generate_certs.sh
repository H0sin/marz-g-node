#!/bin/bash

mkdir -p certs
echo "✅ Generate Certs Folder Success"

echo "💫 START GENERATING"
openssl req -x509 -newkey rsa:4096 -nodes -keyout certs/server.key \
-out certs/server.crt -days 365 \
-subj "/CN=grpc-server"
echo "💫 FINISH GENERATING"

echo "✅ Certificates generated in ./certs"
