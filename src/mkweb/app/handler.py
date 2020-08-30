import os
import tarfile
import sys


def produce(input, output):
    # Producing the website
    os.chdir(input)
    os.system(f'mkdocs build -d {output} -q')

    # Compressing the documentation...
    with tarfile.open(fileobj=sys.stdout.buffer, mode='w|gz') as tar:
        tar.add('.')

    # Website produced correctly


def serve(host, port, path):
    with tarfile.open(fileobj=sys.stdin.buffer, mode='r|gz') as tar:
        tar.extractall(path=path)

    os.chdir(path)
    print('Starting MKDocs')
    os.system(f'mkdocs serve -a {host}:{port}')
