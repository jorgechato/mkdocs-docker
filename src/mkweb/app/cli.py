import click
from app import handler


@click.group(invoke_without_command=False)
def cli():
    pass


@cli.command('produce', help='Produce the website')
@click.option(
    '--input', '-i',
    envvar='DOCS_DIRECTORY',
    required=False,
    type=click.Path(),
)
@click.option(
    '--output', '-o',
    envvar='DOCS_BUILD',
    required=False,
    type=click.Path(),
)
def produce(input, output):
    handler.produce(input, output)
