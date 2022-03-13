import click
from commands import add

@click.group(help='CLI tool to help you stay in touch with your friends')
def cli():
    pass


cli.add_command(add.add)


if __name__ == '__main__':
    cli()
