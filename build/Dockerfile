FROM python:3.8-alpine as builder

ARG MKDOCS_VERSION=1.1.2

RUN apk add -U --no-cache \
    gcc \
    libc-dev \
    ca-certificates

RUN pip install --prefix=/install \
    --no-warn-script-location \
    importlib_metadata \
    mkdocs==${MKDOCS_VERSION} \
    click


FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV DOCS_DIRECTORY="/mkdocs"
ENV DOCS_BUILD="/tmp/out"
ENV HOST="0.0.0.0"
ENV PORT="8000"

ADD src /

COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /install /usr/local

EXPOSE 8000

ENTRYPOINT ["mkweb"]
