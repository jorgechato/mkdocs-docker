# Jorge Chato Astrain - Infrastructure Engineer, SRE/Ops

## Build

```bash
$ docker build -t mkdocs -f build/Dockerfile .
# with Mkdocs version argument
$ docker build --build-arg MKDOCS_VERSION=1.1.2 -t mkdocs -f build/Dockerfile .
```

## Run

### Produce

```bash
$ docker run -i --rm -a stdout -v <mkdocs-project-folder>:/mkdocs mkdocs produce > /tmp/out-docker.tar.gz
```

### Serve

```bash
```

## CI/CD
