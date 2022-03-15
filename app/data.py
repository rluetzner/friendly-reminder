import os
import jsonpickle
from app import constants


class friend:

    def __init__(self, name, reminder_days, last_contact):
        self.name = name
        self.reminder_days = reminder_days
        self.last_contact = last_contact

class data:

    def __init__(self):
        self.friends = []

    def save(self):
        if not os.path.exists(constants.CONFIG_DIR):
            os.mkdir(constants.CONFIG_DIR)
        with open(constants.DATA_FILE_PATH, 'w') as f:
            f.write(jsonpickle.encode(self, indent=4, unpicklable=False))


def load():

    if os.path.isfile(constants.DATA_FILE_PATH):
        with open(constants.DATA_FILE_PATH, 'r') as f:
            dec = jsonpickle.decode(f.read())
            d = data()
            for f in dec['friends']:
                d.friends.append(friend(f['name'], f['reminder_days'], f['last_contact']))
            return d
    else:
        return data()
