import click
from app import data
from datetime import date,datetime


@click.command(short_help='Check reminders for today')
@click.option('--all', help='Include friends you contacted recently', is_flag=True)
def check(all):
    today = date.today()
    
    def days_remaining(friend):
        last = datetime.strptime(friend.last_contact, '%Y-%m-%d').date()
        delta = today - last
        return friend.reminder_days - delta.days


    d = data.load()
    friends = {f.name: days_remaining(f)  for f in d.friends}
    if not all:
        new_friends = {}
        for f in friends:
            remaining_days = friends[f]
            if remaining_days <= 0:
                new_friends[f] = friends[f]
        friends = new_friends
    
    def get_order(k):
        return friends[k]

    lst = sorted([f for f in friends], key=get_order)
    if lst:
        print('Think about contacting:')
        for l in lst:
            print(f'{l} ({friends[l]} days)')
    else:
        print('Nothing for today.')
