import os
import jsonpickle
from pathlib import Path


class friend:

    def __init__(self, name, reminder_days, last_contact):
        self.name = name
        self.reminder_days = reminder_days
        self.last_contact = last_contact

class data:

    def __init__(self):
        self.friends = []

    def save(self):
        home = Path.home()
        parent_dir = f'{home}/.config/friendly-reminder'
        if not os.path.exists(parent_dir):
            os.mkdir(parent_dir)
        file_path = f'{parent_dir}/data.json'
        with open(file_path, 'w') as f:
            f.write(jsonpickle.encode(self, indent=4, unpicklable=False))


def load():

    home = Path.home()
    file_path = f'{home}/.config/friendly-reminder/data.json'
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            dec = jsonpickle.decode(f.read())
            d = data()
            for f in dec['friends']:
                d.friends.append(friend(f['name'], f['reminder_days'], f['last_contact']))
            return d
    else:
        return data()
