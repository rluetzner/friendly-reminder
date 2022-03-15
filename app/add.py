import click
from app import data
from app import config
from datetime import date


@click.command(short_help='Add a new contact')
@click.option('--name', help='The name of the person you want to stay in touch with', required=True)
@click.option('--days', help='How many days between reminders', type=int)
def add(name, days):
    d = data.load()
    if any(filter(lambda f: f.name == name, d.friends)):
        raise click.UsageError(f'{name} is already in the reminder list.')
    c = config.load_config()
    today = date.today()
    day = today.strftime('%Y-%m-%d')
    if not days:
        days = c.default_days
    d.friends.append(data.friend(name, days, day))
    d.save()
    print(f'Added {name} succesfully.')
