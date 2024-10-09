import argparse
import commands.config as conf
import commands.init as init

def check_status(args):

    access_token = conf.get_access_token()

    print(access_token)
