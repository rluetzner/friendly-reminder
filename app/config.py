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
    parent_dir = f'{home}/.config/friendly-reminder'
    file_path = f'{parent_dir}/friendly-reminder.yml'
    if os.path.isfile(file_path):
        return read_yaml(file_path)
    else:
        cfg = config()
        if not os.path.exists(parent_dir):
            os.mkdir(parent_dir)
        write_yaml(file_path, cfg)
        return cfg
