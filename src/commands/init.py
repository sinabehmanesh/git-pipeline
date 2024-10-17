from datetime import datetime
from colorama import Fore, Style, init

try:
    from config import *
except ImportError:
    from .config import *


def init_git_config(args) -> dict:

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
