import click


@click.command()
@click.option('--name', help='The name of the person you want to stay in touch with', required=True)
def add(name):
    print(f'You added {name} succesfully.')
