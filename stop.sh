#!/bin/bash
cd "$(dirname "$0")"
echo "Stop containers"
docker-compose stop

echo "Remove containers"
docker-compose down --volumes --remove-orphans  --rmi all