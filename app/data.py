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
        file_path = f'{home}/.config/friendly-reminder/data.json'
        with open(file_path, 'w') as f:
            f.write(jsonpickle.encode(self, indent=4))


def load():

    home = Path.home()
    file_path = f'{home}/.config/friendly-reminder/data.json'
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            return jsonpickle.decode(f.read())
    else:
        return data()
