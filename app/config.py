import yaml
import os
from app import constants


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

    if os.path.isfile(constants.CONFIG_FILE_PATH):
        return read_yaml(constants.CONFIG_FILE_PATH)
    else:
        cfg = config()
        if not os.path.exists(constants.CONFIG_DIR):
            os.mkdir(constants.CONFIG_DIR)
        write_yaml(constants.CONFIG_FILE_PATH, cfg)
        return cfg
