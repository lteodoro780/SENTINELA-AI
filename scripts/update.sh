#!/bin/bash

echo "Updating SENTINELA AI containers..."

docker-compose pull
docker-compose up -d

echo "Update completed."
docker ps
