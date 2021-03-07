# ezhacks-app

start up flask app using port 80 [dockerhub link](https://hub.docker.com/repository/docker/nathanesau/ezhacks)

```bash
docker build -t ezhacks-app .

# run the image
docker run -p 80:80 --name ezhacks-app -d ezhacks-app

# push to dockerhub
docker tag ezhacks-app nathanesau/ezhacks:ezhacks-app
docker push nathanesau/ezhacks:ezhacks-app
```

Images:

* [winners](https://user-images.githubusercontent.com/4649987/110227776-c2ffc380-7ec9-11eb-8ea2-7972688efe0f.png)
* [losers](https://user-images.githubusercontent.com/4649987/110227778-c4c98700-7ec9-11eb-93e4-4a2fe123ffb2.png)
* [dramatics](https://user-images.githubusercontent.com/4649987/110227781-c6934a80-7ec9-11eb-8e3b-cbbda8caaded.png)
* [richest](https://user-images.githubusercontent.com/4649987/110227782-c7c47780-7ec9-11eb-8f63-c0ba3bce758a.PNG)