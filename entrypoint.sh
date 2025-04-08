#!/bin/sh

echo "🔧 Generating self-signed cert..."
python3 generate_cert.py

echo "🚀 Starting gRPC server..."
python3 main.py
