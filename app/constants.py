import os
from pathlib import Path


HOME = Path.home()
CONFIG_DIR = os.path.join(HOME, '.config', 'friendly-reminder')
DATA_FILE_PATH = os.path.join(CONFIG_DIR, 'data.json')
CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, 'friendly-reminder.yml')
