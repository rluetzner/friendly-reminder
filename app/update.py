import click
from app import data
from datetime import datetime


@click.command()
@click.option('--name', help='The name of the person you want to update', required=True)
@click.option('--new-name', help='A new name for the friend')
@click.option('--days', help='How many days between reminders', type=int)
@click.option('--last-contact', help='Date of your last contact in the format yyyy-mm-dd')
def update(name, new_name, days, last_contact):
    d = data.load()
    friend = next(filter(lambda f: f.name == name, d.friends), None)
    if not friend:
        raise click.UsageError(f'{name} is not in the reminder list.')
    if any(filter(lambda f: f.name == new_name, d.friends)):
        raise click.UsageError(f'{new_name} is already in the reminder list.')
    if new_name:
        friend.name = new_name
    if days:
        friend.reminder_days = days
    if last_contact:
        try:
            date = datetime.strptime(last_contact, '%Y-%m-%d')
            friend.last_contact = last_contact
        except:
            raise click.UsageError(f'{last_contact} is not a valid date as yyyy-mm-dd.')
    d.save()
    print(f'Updated {name} succesfully.')
