#!/bin/sh

echo "✅ Install Packages iproute2 wireguard wireguard-tools iptables"
apt-get update && \
apt-get install -y wireguard wireguard-tools

echo "🔧 Generating self-signed cert..."
python3 generate_cert.py

echo "🚀 Starting gRPC server..."
python3 main.py