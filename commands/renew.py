import click
import data
import config
from datetime import date


@click.command()
@click.option('--name', help='The name of the person you contacted', required=True)
def renew(name):
    d = data.load()
    friend = next(filter(lambda f: f.name == name, d.friends), None)
    if not friend:
        raise click.UsageError(f'{name} is not in the reminder list.')
    c = config.load_config()
    today = date.today()
    day = today.strftime('%Y-%m-%d')
    friend.last_contact = day
    d.save()
    print(f'Updated {name} succesfully.')
