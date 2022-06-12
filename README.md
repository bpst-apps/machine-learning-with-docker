# Machine Learning with Docker


To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = bpst.web@gmail.com
2. HEROKU_API_KEY = 4538b09c-a457-428a-b411-2868e3d79837
3. HEROKU_APP_NAME = ml-regression-app


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```

