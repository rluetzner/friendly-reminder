import click
import config
from commands import add

@click.group(help='CLI tool to help you stay in touch with your friends')
def cli():
    pass


cli.add_command(add.add)


if __name__ == '__main__':
    cfg = config.load_config()
    print(cfg.yaml())
    cli()
