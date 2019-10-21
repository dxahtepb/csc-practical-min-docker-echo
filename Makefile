build:
	docker build . -t my_server:1

start:
	docker run -d --rm -p 65432:65432 my_server:1 > .id

stop:
	docker stop `cat .id`; mv .id .id.used

clean:
	rm -f .id.used