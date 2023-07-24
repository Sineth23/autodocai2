
import os
from pathlib import Path

user_config_file_name = 'autodoc.user.json'
user_config_file_path = Path(os.path.expanduser('~'), '.config', 'autodoc', user_config_file_name)
