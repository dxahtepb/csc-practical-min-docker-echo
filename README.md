# Simple echo server

Server listens on port 65432 and answers to message \<msg\> with "OK: \<msg\>". One connected client per time.

### Run steps

1. Install [docker](https://www.docker.com/).
2. Run `make build` to build a container image.
3. Run `make start` to start a new container with running server from the image.
4. Run `make stop` to stop the container.
5. Run `make clean` to clean up temporary files.
