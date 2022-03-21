import click
from app import data
from datetime import date


@click.command(short_help='Remove a contact from the reminder list')
@click.option('--name', help='The name of the person to remove', required=True)
def remove(name):
    d = data.load()
    friend = next(filter(lambda f: f.name == name, d.friends), None)
    if friend:
        d.friends.remove(friend)
    d.save()
    print(f'Removed {name} succesfully.')
