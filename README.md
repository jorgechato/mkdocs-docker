# Mkdocs on Doker

## Build

One of the most challenging things about building images is keeping the image
size down.
In order to build the most efficient Docker image I used alpine as base.
Mkdocs and the wrapper script runs over python so the next layer will be
python-3.8.

As we need to build Mkdocs and we don't want the build dependencies be present
in our final image let's use docker multistage, where the build layer will be in
charge of building the mkdocs tool and copy it from the final layer.

If we move from python to Go we can stretch the size of the image even more but
for the sake of consistency on the code let's keep it as python script.

```bash
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
mkdocs              latest              c043eb01bd79        50 seconds ago      90MB
<none>              <none>              aef1f9e12827        53 seconds ago      244MB
python              3.8-alpine          44fceb565b2a        2 weeks ago         42.7MB
```

As we can see above python image is 42.7MB, the final mkdocs images is 83MB
while the build image which we don't need from now on is 244MB. We reduce the
final image size by 154MB.

```bash
$ docker build -t mkdocs -f build/Dockerfile .
# with Mkdocs version argument
$ docker build --build-arg MKDOCS_VERSION=1.1.2 -t mkdocs -f build/Dockerfile .
```

## Run

As the tool need a few parameter we can specify it as env variables in the
container but also we can pass them as arguments of the wrapper.

```bash
# produce
$ ... produce --help
Usage: mkweb produce [OPTIONS]

  Produce the website

Options:
  -i, --input PATH
  -o, --output PATH
  --help             Show this message and exit.

# serve
$ ... serve --help
Usage: mkweb serve [OPTIONS]

  Serve the website

Options:
  -h, --host TEXT
  -p, --port TEXT
  --path PATH
  --help           Show this message and exit.
```

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

### Integration Test

**Dependencies**

- mkdocs

```bash
$ python src/mkweb/app/handler_test.py
```

## CI/CD

The Jenkinsfile is ready to work as multibranch pipeline.
If you don't have a Jenkins instance run:

```bash
$ docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v /tmp/jenkins:/var/jenkins_home jenkins/jenkins:lts
```

In order to pull from a private repository you will need to generate a new
Github token and add it as secret in Jenkins. We will use ID=`github_credential`.
Keep in mind to set the proper scope for the token.

**Dependencies**

- [Docker pipeline](https://plugins.jenkins.io/docker-workflow/#documentation)

To produce to quay.io we need to set a new credential too, let's use the
ID=`quay_credential` for that.
