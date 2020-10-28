flaskAppExists=$( docker ps -aq -f name=flask-waitress_web_1 )
if [ -z "$flaskAppExists" ]; then
    docker-compose up --remove-orphans --build --force-recreate --no-start
fi

echo "Start docker container"
docker-compose start