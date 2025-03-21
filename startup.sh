#!/bin/bash

echo "🔐 Loading secrets from Google Secret Manager..."

python load_secrets_gcp.py

echo "🚀 Launching the AI Text Processing Pipeline..."

# Start your app (can be modified for streamlit, fastapi, etc.)
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
