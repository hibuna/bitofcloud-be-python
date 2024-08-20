# bitofcloud
<hr>

Open source cloud storage.

This repo is part of the fullstack bitofcloud project. This repository is the main repository and contains everything 
needed for development and deployment.

bitofcloud is a passion project. The goal is to develop an enterprise grade RESTful application using the following technologies:
- Linux
- Docker
- PostgreSQL
- Python3
- Vue.js


## Setup
<hr>


### Install requirements
See [Docker](https://docs.docker.com/engine/install/debian/) and [Docker Compose](https://docs.docker.com/compose/install/)


### Setup hot reloading for frontend development
- Clone the [frontend repo](https://github.com/hibuna/bitofcloud-fe-vue) from GitHub
- Set `PATH_TO_FRONTEND_REPO` in `.env`


### Copy .dist files
Configurations and secrets are mostly private. To share a template for these type of files,
distributables are used. These files end with `.dist`. For each of these files,
copy it to a file without that ending. For example:

```
$ cp file.ext.dist file.ext
```


### Initialize local development server
```
$ dev/init
```


## Deployment (local)
<hr>

### Start development server
A wrapper for docker compose up
```
$ dev/start
```

### Stop development server
A wrapper for docker compose down
```
$ dev/stop
```

### Restart development server
```
$ dev/restart
```

### Hard reset environment
```
$ dev/reset
```

For persisting issues, try:
```
$ dev/nuke && dev/init
```

### Migrations
A wrapper for alembic
```
$ dev/migrations
```

### Print container logs
```
$ dev/log
```