#!/bin/bash

mkdir -p certs

openssl req -x509 -newkey rsa:4096 -nodes -keyout certs/server.key \
-out certs/server.crt -days 365 \
-subj "/CN=grpc-server"

echo "✅ Certificates generated in ./certs"
