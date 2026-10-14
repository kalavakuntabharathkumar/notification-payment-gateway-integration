#!/usr/bin/env bash
set -e
sudo apt-get update -y
sudo apt-get install -y docker.io docker-compose-plugin
sudo systemctl enable --now docker
# Copy .env and application image/configuration before starting production containers.
