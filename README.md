# trello
Exercise trello app

# How to install
This project use `docker` to work. Please refer to https://docs.docker.com/engine/install/ in order to check how install `docker` on your system

**Run the next commands:**

```shell
docker compose build
docker compose up -d
```

All images will be downloaded, it will take time, when it will be finished please write
```shell
docker compose ps
```
You will see the next prompt. Go to http://localhost:8000 on your browser.

```shell
NAME                              IMAGE                           COMMAND                  SERVICE             CREATED             STATUS              PORTS
trello-backend-postgres-1         postgres:latest                 "docker-entrypoint.s…"   postgres            9 minutes ago       Up 9 minutes        0.0.0.0:5432->5432/tcp, :::5432->5432/tcp
trello-backend-trello-backend-1   trello-backend-trello-backend   "/docker-entrypoint.…"   trello-backend      9 minutes ago       Up 9 minutes        0.0.0.0:8000->8000/tcp, :::8000->8000/tcp
```
