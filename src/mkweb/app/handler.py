import os
import tarfile
import sys


def produce(input, output, fileobj=sys.stdout.buffer, fileto=None):
    """
    Produce the web from a mkdocs folder

    param: input: mkdocs project path
    param: output: tmp path for rendered web
    param: fileobj: output object for dependency injection in tarfile
    param: fileto: input file if fileobj isn't sys.stdin
    return: stdout binary
    """
    # Producing the website
    os.chdir(input)
    os.system(f'mkdocs build -d {output} -q')

    # Compressing the documentation...
    with tarfile.open(fileto, fileobj=fileobj, mode='w|gz') as tar:
        tar.add('.')

    # Website produced correctly


def serve(host, port, path, fileobj=sys.stdin.buffer, filefrom=None):
    """
    Serve the documentation page from sdtin binary

    param: host: host of the server, default 0.0.0.0
    param: port: port of the server, default:8000
    param: path: tmp path to write the tar file
    param: fileobj: output object for dependency injection in tarfile
    param: filefrom: input file if fileobj isn't sys.stdin
    """
    with tarfile.open(filefrom, fileobj=fileobj, mode='r|gz') as tar:
        tar.extractall(path=path)

    os.chdir(path)
    print('Starting MKDocs')
    os.system(f'mkdocs serve -a {host}:{port}')
