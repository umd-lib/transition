# In Transition Static web-app

Static web-app of in transition website.
Jira: https://issues.umd.edu/browse/LIBWEB-4961

## Build Operations

To spin up a docker container of the static app, build the dockerfile
```
docker build -t <transition image name> .
```
where <transition image name> is the image name.


To run the container from built image on desired port(Say 8000),
```
docker run  -p <desired port>:80 <transition image name>
```

##Example

To spin up a container in port 8000.

```
docker build -t transition .
docker run  -p 8000:80 transition
```