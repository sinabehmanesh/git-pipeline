import argparse
from colorama import Fore, Style, init

import commands.init as initialize

def hell():
    print("hi")

def main():

    parser = argparse.ArgumentParser(description="Simply check your pipeline with one command")

    subparser = parser.add_subparsers(dest="command", help="available command")


    #commands definition
    init_parser = subparser.add_parser('init', help="check status")

    
    args = parser.parse_args()

    commands = {
        'init': initialize.check_git_config
    }

    if args.command in commands:
        commands[args.command]()
    else:
        parser.print_help()
        


if __name__ == "__main__":

    # Initialize colorama
    init(autoreset=True)

    main()