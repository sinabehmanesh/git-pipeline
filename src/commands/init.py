import subprocess
from datetime import datetime
from colorama import Fore, Style, init

try:
    from config import *
except ImportError:
    from .config import *

def check_git_branch() -> str:
    try:
        branch_name = subprocess.check_output(['git', 'branch', '--show-current'],
                                              stderr=subprocess.STDOUT).strip().decode('utf-8')
        return branch_name
    except subprocess.CalledProcessError as e:
        print(Fore.RED + "Error: {e.output.decode('ufw-8')}")
        return None
        
def check_git_origin() -> str:
    try:
        origin = subprocess.check_output(['git', 'remote', 'get-url', 'origin'],
                                         stderr=subprocess.STDOUT).strip().decode('utf-8')
        return origin
    except subprocess.CalledProcessError as e:
        print(Fore.RED + "Error: {e.output.deocde('utf-8')}")
        return None
    
def check_git_username() -> str:
    try:
        origin = subprocess.check_output(['git', 'config', 'user.name'],
                                         stderr=subprocess.STDOUT).strip().decode('utf-8')
        return origin
    except subprocess.CalledProcessError as e:
        print(Fore.RED + "Error: {e.output.deocde('utf-8')}")
        return None

def check_git_email() -> str:
    try:
        origin = subprocess.check_output(['git', 'config', 'user.email'],
                                         stderr=subprocess.STDOUT).strip().decode('utf-8')
        return origin
    except subprocess.CalledProcessError as e:
        print(Fore.RED + "Error: {e.output.deocde('utf-8')}")
        return None

def check_git_config() -> dict:

    # Get Current date time
    currentDate = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    
    branch = check_git_branch()
    origin = check_git_origin()
    username = check_git_username()
    email = check_git_email()

    if check_config_exists():

        access_token = get_access_token()

        gitinfo = {
        "origins": {
            origin: {
            "branch" : branch,
            "token": access_token,
            "username": username,
            "email": email,
            "updatedAt": currentDate
            }
        }
        }

        update_config(gitinfo)
        return gitinfo

    else:

        gitinfo = {
        "origins": {
            origin: {
            "branch" : branch,
            "token": "NOT SET",
            "username": username,
            "email": email,
            "updatedAt": currentDate
            }
        }
        }
        update_config(gitinfo)

        print(Fore.GREEN + "Configuration created")
        print("Please provide access token in ~/.gitpipeline/config.yaml")
        return gitinfo