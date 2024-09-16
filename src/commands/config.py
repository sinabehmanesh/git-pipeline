import os
from pathlib import Path
import yaml

def check_config_exists() -> bool:

    homedir = f'{os.path.expanduser("~")}/.gitpipeline'

    if os.path.isdir(f"{homedir}/.gitpipeline"):
        if os.path.isfile(f"{homedir}/config.yaml"):
            return True
        else:
            return False
    else:
        Path(homedir).mkdir(parents=True, exist_ok=True)
        return False


def create_config(data) -> str:

    homedir = f'{os.path.expanduser("~")}/.gitpipeline'

    with open(f'{homedir}/config.yaml', 'w') as yaml_config:
        yaml.dump(data, yaml_config)


def get_access_token() -> str:
    pass

def show_config() -> str:
    pass