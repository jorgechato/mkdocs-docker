# docker run -i --rm -a stdout -v /tmp/mkdocs:/mkdocs mkdocs produce > /tmp/out-docker.tar.gz

# cat /tmp/out-docker.tar.gz | docker run -i --rm -a stdin -p 8000:8000 --name mkdocs mkdocs serve
