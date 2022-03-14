import yaml
import os
from pathlib import Path


class config:

    def __init__(self):
        # Default number of days after which reminders will be shown.
        self.default_days = 7

    def yaml(self):
        return yaml.dump(self.__dict__)

    def load(self, data):
        values = yaml.safe_load(data)
        self.default_days = values['default_days']


def load_config():

    def read_yaml(file):
        with open(file, 'r') as f:
            cfg = config()
            cfg.load(f.read())
            return cfg

    def write_yaml(file, cfg):
        with open(file, 'w') as f:
            f.write(cfg.yaml())

    home = Path.home()
    file_path = f'{home}/.config/friendly-reminder/friendly-reminder.yml'
    if os.path.isfile(file_path):
        return read_yaml(file_path)
    else:
        cfg = config()
        write_yaml(file_path, cfg)
        return cfg
