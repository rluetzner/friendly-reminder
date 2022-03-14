import click
import config
from commands import add
from commands import check
from commands import renew
from commands import update

@click.group(help='CLI tool to help you stay in touch with your friends')
def cli():
    pass


cli.add_command(add.add)
cli.add_command(check.check)
cli.add_command(renew.renew)
cli.add_command(update.update)


if __name__ == '__main__':
    cli()
