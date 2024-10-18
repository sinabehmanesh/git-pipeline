import os
import yaml
import subprocess
import re

from pathlib import Path
from colorama import Fore, Style

import commands.init as init


def check_git_domain() -> str:
    git_domain_name = extract_domain()
    if git_domain_name is None:
        print("Can not detect GIT domain")
        SystemExit(1)
    else:
        return git_domain_name


def check_git_branch() -> str:
    try:
        branch_name = (
            subprocess.check_output(
                ["git", "branch", "--show-current"], stderr=subprocess.STDOUT
            )
            .strip()
            .decode("utf-8")
        )
        return branch_name
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error: {e.output.decode('utf-8')}")
        return None


def check_git_origin() -> str:
    try:
        origin = (
            subprocess.check_output(
                ["git", "remote", "get-url", "origin"],
                stderr=subprocess.STDOUT,
            )
            .strip()
            .decode("utf-8")
        )
        return origin
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error: {e.output.decode('utf-8')}")
        return None


def check_git_repo_name() -> str:
    try:
        result = subprocess.check_output(
            "basename `git rev-parse --show-toplevel`", shell=True
        )
        repo_name = result.decode("utf-8").strip()
        return repo_name
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        return None


# Call this function using check_git_domain function.
def extract_domain():
    remote_url = check_git_origin()

    ssh_pattern = r"@([^:]+)"
    https_pattern = r"https://([^/]+)"

    # Check if the URL is in SSH format
    ssh_match = re.search(ssh_pattern, remote_url)
    if ssh_match:
        return ssh_match.group(1)

    # Check if the URL is in HTTPS format
    https_match = re.search(https_pattern, remote_url)
    if https_match:
        return https_match.group(1)

    # Return None if no match
    return None


# This is for the api check, if its GitHub oder GitLab
def check_git_api_type() -> str:
    # check if the ssh url belongs to a GitHub or GitLab.
    # Idk how to do it.
    return "github"


def check_git_username() -> str:
    try:
        origin = (
            subprocess.check_output(
                ["git", "config", "user.name"], stderr=subprocess.STDOUT
            )
            .strip()
            .decode("utf-8")
        )
        return origin
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error: {e.output.decode('utf-8')}")
        return None


def check_git_email() -> str:
    try:
        origin = (
            subprocess.check_output(
                ["git", "config", "user.email"], stderr=subprocess.STDOUT
            )
            .strip()
            .decode("utf-8")
        )
        return origin
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error: {e.output.decode('utf-8')}")
        return None


def check_config_exists() -> bool:
    # Check if config directory and config file exist
    homedir = f'{os.path.expanduser("~")}/.gitpipeline'

    if os.path.isdir(f"{homedir}"):
        if os.path.isfile(f"{homedir}/config.yaml"):
            return True
        else:
            with open(f"{homedir}/config.yaml", "w"):
                return False
    else:
        Path(homedir).mkdir(parents=True, exist_ok=True)
        with open(f"{homedir}/config.yaml", "w"):
            return False


def update_config(data) -> str:
    homedir = f'{os.path.expanduser("~")}/.gitpipeline'

    for origin_key in data["origins"]:
        data_origin = origin_key

    with open(f"{homedir}/config.yaml", "r+") as yaml_file:
        try:
            yaml_data = yaml.safe_load(yaml_file) or {}
        except yaml.YAMLError:
            print(
                Fore.RED
                + "\033[1mERROR:"
                + Style.NORMAL
                + " Wrong yaml indentation, please check the configuration"
            )
            raise SystemExit
        if yaml_data is None or yaml_data == {}:
            print(Fore.LIGHTYELLOW_EX + "Config file was empty!")
            with open(f"{homedir}/config.yaml", "w") as file:
                file.truncate()
                yaml.dump(data, file, default_flow_style=False)

        elif isinstance(yaml_data, dict):
            for _, value in yaml_data.items():
                for item in value:
                    if item == data_origin:
                        # Now it will update the origin data
                        with open(f"{homedir}/config.yaml", "w") as file:
                            yaml_data["origins"][item].update(
                                data["origins"][item]
                            )
                            yaml.dump(
                                yaml_data, file, default_flow_style=False
                            )
                            print("Origin Updated!")

                    else:
                        print("origin does not exist")
                        with open(f"{homedir}/config.yaml", "a") as file:
                            yaml.dump(data, file, default_flow_style=False)
        else:
            print("what?")


def get_access_token() -> str:
    homedir = f'{os.path.expanduser("~")}/.gitpipeline'
    yaml_file = Path(f"{homedir}/config.yaml")

    # Define Global use of access_token variable
    access_token = None

    origin_name = init.check_git_origin()

    if check_config_exists():
        try:
            with yaml_file.open("r") as file:
                data = yaml.safe_load(file)

                if origin_name in data["origins"]:
                    access_token = data["origins"][origin_name]["token"]

        except KeyError as e:
            return f"Invalid YAML structure. Missing key: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

        return access_token

    else:
        print(
            Fore.RED
            + "\033[1mERROR:"
            + Style.NORMAL
            + " Config file not found, run gp init or restore your backup!"
        )
        raise SystemExit(1)


def show_config() -> str:
    pass
