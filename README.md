# Jorge Chato Astrain - Infrastructure Engineer, SRE/Ops

## Build

```bash
$ docker build -t mkdocs -f build/Dockerfile .
# with Mkdocs version argument
$ docker build --build-arg MKDOCS_VERSION=1.1.2 -t mkdocs -f build/Dockerfile .
```

## Run

```bash
DOCS_DIRECTORY="/mkdocs"
DOCS_BUILD="/tmp/out"
HOST="0.0.0.0"
PORT="8000"
```

### Produce

```bash
$ docker run -i --rm -a stdout -v <mkdocs-project-folder>:/mkdocs mkdocs produce > /tmp/out-docker.tar.gz
```

### Serve

```bash
$ cat <file.tar.gz> | docker run -i --rm -a stdin -p 8000:8000 --name mkdocs mkdocs serve
```

## CI/CD
