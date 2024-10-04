import os
import yaml
from pathlib import Path
from colorama import Fore, Style, init


def check_config_exists() -> bool:
    #Check if config directory and config file exist
    homedir = f'{os.path.expanduser("~")}/.gitpipeline'

    if os.path.isdir(f"{homedir}"):
        if os.path.isfile(f"{homedir}/config.yaml"):
            return True
        else:
            with open(f'{homedir}/config.yaml', 'w'):
                return False
    else:
        Path(homedir).mkdir(parents=True, exist_ok=True)
        with open(f'{homedir}/config.yaml', 'w'):
            return False


def update_config(data) -> str:

    homedir = f'{os.path.expanduser("~")}/.gitpipeline'

    for origin_key in data["origins"]:
        data_origin = origin_key

#TODOS: we should add check if the given origin exists in the current configuration, if not, append a new origin
    with open(f'{homedir}/config.yaml', 'r+') as yaml_file:

        try:
            yaml_data = yaml.safe_load(yaml_file) or {}
        except yaml.YAMLError:
            print(Fore.RED + "\033[1mERROR:" + Style.NORMAL + " Wrong yaml file indentation, please double check the configuration")
            raise SystemExit
        if yaml_data is None or yaml_data == {}:
            print(Fore.LIGHTYELLOW_EX + "Config file was empty!")
            with open(f'{homedir}/config.yaml', 'w') as file:
                file.truncate()
                yaml.dump(data, file, default_flow_style=False)

        elif isinstance(yaml_data, dict):
            for _, value in yaml_data.items():
                for item in value:
                    if item == data_origin:
                        #Now it will update the origin data
                        with open(f'{homedir}/config.yaml', 'w') as file:
                            yaml_data['origins'][item].update(data['origins'][item])
                            yaml.dump(yaml_data, file, default_flow_style=False)
                            print("Origin Updated!")

                    else:
                        print("origin does not exist")
                        with open(f'{homedir}/config.yaml', 'a') as file:
                            yaml.dump(data, file, default_flow_style=False)
        else:
            print("what?")

def get_access_token() -> str:
    return "thisistestaccesstoken"

def show_config() -> str:
    pass