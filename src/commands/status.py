import commands.config as conf


def check_status(args):
    access_token = conf.get_access_token()

    print(access_token)
