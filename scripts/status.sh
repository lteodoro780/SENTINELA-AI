#!/bin/bash

echo "=================================="
echo "SENTINELA AI - Docker Status"
echo "=================================="

docker ps

echo ""
echo "=================================="
echo "Docker Images"
echo "=================================="

docker images

echo ""
echo "=================================="
echo "Docker Networks"
echo "=================================="

docker network ls
