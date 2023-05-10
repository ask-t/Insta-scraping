# Analytics-selenium- for instagram

This app get the instagram information (Date, Like count, contents, URL), then add those information in csv. The app requires to use Docker. If you don’t have Docker, please download this first.

## Language and Framework

Python 3 

Docker

## build docker image

```bash
docker image build -t analytics .
```

## Run

```bash
docker run -it --rm analytics /bin/bash
```

## Check Container ID

```bash
docker ps -a
```

## Copy csv file

```bash
docker cp <CONTAINER ID>:app/instainfo.csv <your pc's path>
```
