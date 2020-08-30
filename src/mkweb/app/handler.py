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
