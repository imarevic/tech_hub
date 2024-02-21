#### Commands to work with Docker on Linux

The following is to give your user enough rights to interact with docker engine on linux:

```
sudo usermod -aG docker ${USER}
```

then add user to su:

```
su - ${USER}
```

---

These commands are mainly for local testing:

Bring down any running containers with volumes:

```
docker-compose down -v
```

Rund ocker compose wiht building new dev images locally:

```
docker-compose up -d --build
```

List all ***running*** containers:

```
docker ps
```

List all containers (running and stopped):

```
docker ps -a
```

Inspect a container by name:

```
docker inspect <container-name>
``` 

Inspect logs of a container:

```
docker logs <container_id>
```