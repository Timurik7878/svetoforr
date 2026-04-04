#!/bin/bash

sudo apt update && sudo apt install nginx curl -y
curl -L --output cloudflared.deb https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb
python3 -m venv venv
source venv/bin/activate
