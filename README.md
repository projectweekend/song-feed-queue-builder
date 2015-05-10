### Build a Docker image
```
docker build -t name_of_image .
```


### Start service in a container
```
docker run -e AWS_ACCESS_KEY_ID=accessid -e AWS_SECRET_ACCESS_KEY=accesskey name_of_image
```

#### Required environment variables

* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`
