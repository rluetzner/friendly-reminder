import click
import data
import config
from datetime import date


@click.command()
@click.option('--name', help='The name of the person you want to stay in touch with', required=True)
def add(name):
    d = data.load()
    if any(filter(lambda f: f.name == name, d.friends)):
        raise click.UsageError(f'{name} is already in the reminder list.')
    c = config.load_config()
    today = date.today()
    day = today.strftime('%Y-%m-%d')
    d.friends.append(data.friend(name, c.default_days, day))
    d.save()
    print(f'You added {name} succesfully.')
