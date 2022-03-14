import click
import data
import config
from datetime import datetime


@click.command()
@click.option('--name', help='The name of the person you want to update', required=True)
@click.option('--new-name', help='A new name for the friend')
@click.option('--days', help='How many days between reminders')
@click.option('--last-contact', help='Date of your last contact in the format yyyy-mm-dd')
def update(name, new_name, days, last_contact):
    d = data.load()
    friend = next(filter(lambda f: f.name == name, d.friends), None)
    if not friend:
        raise click.UsageError(f'{name} is not in the reminder list.')
    c = config.load_config()
    if new_name:
        friend.name = new_name
    if days:
        try:
            friend.reminder_days = int(days)
        except:
            raise click.UsageError(f'{days} is not a valid number.')
    if last_contact:
        try:
            date = datetime.strptime(last_contact, '%Y-%m-%d')
            friend.last_contact = last_contact
        except:
            raise click.UsageError(f'{last_contact} is not a valid date as yyyy-mm-dd.')
    d.save()
    print(f'Updated {name} succesfully.')
