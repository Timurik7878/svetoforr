#!/bin/bash

source venv/bin/activate
docker run --name pedantic_lovelace
sudo docker run -p 8080:80 nginx
clouflared tunnel --url http://localhost:80