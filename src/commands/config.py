import os
from pathlib import Path
import yaml

def check_config_exists() -> bool:
    #Check if config directory and config file exist
    homedir = f'{os.path.expanduser("~")}/.gitpipeline'

    if os.path.isdir(f"{homedir}"):
        if os.path.isfile(f"{homedir}/config.yaml"):
            return True
        else:
            return False
    else:
        Path(homedir).mkdir(parents=True, exist_ok=True)
        return False


def update_config(data) -> str:

    homedir = f'{os.path.expanduser("~")}/.gitpipeline'

    for origin_key in data["origins"]:
        data_origin = origin_key

#TODOS: we should add check if the given origin exists in the current configuration, if not, append a new origin
    with open(f'{homedir}/config.yaml', 'r+') as yaml_config:
        yaml_data = yaml.safe_load(yaml_config)
        if isinstance(yaml_data, dict):
            for key, value in yaml_data.items():
                for item in value:
                    if item == data_origin:
                        print("config exists")
                # if isinstance(value, dict):
                #     # This means the current key has nested keys (layer 2)
                #     for sub_key in value.keys():
                #         if {sub_key} == data_origin:
                #             print("configuration already exist for this origin")
                #             print(sub_key)
                #         else:
                #             print(f"Could not find configuration for this origin")
                #             print(f"{data_origin} not found")
                # else:
                #     print(f"Could not find configuration for this origin")

        yaml.dump(data, yaml_config)


def get_access_token() -> str:
    return "thisistestaccesstoken"

def show_config() -> str:
    pass