# flask-waitress

## Start development server
The `docker-compose.yml` runs the container in development mode on port 5000 with hot reloading
```sh
./start.sh
```

Visit
```sh
curl "http://0.0.0.0:5000/?number=2"
```

## Stop/ remove containers
```sh
./stop.sh
```


### References/ alternatives
- Docker docs [Get started with Docker Compose](https://docs.docker.com/compose/gettingstarted/)
- Flask [Deploy to Production](https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/)
    ```sh
    web_1  |    WARNING: This is a development server. Do not use it in a production deployment.
    web_1  |    Use a production WSGI server instead.
    ```
- Alternatively use [FastAPI](https://fastapi.tiangolo.com/)
- ...
