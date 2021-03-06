import click
from app import add
from app import check
from app import remove
from app import renew
from app import update

@click.group(help='CLI tool to help you stay in touch with your friends')
@click.version_option(package_name='friendly-reminder')
def cli():
    pass


cli.add_command(add.add)
cli.add_command(check.check)
cli.add_command(remove.remove)
cli.add_command(renew.renew)
cli.add_command(update.update)


if __name__ == '__main__':
    cli()
