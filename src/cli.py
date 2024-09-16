import argparse

import commands.init as init

def hell():
    print("hi")

def main():

    parser = argparse.ArgumentParser(description="Simply check your pipeline with one command")

    subparser = parser.add_subparsers(dest="command", help="available command")


    #commands definition
    init_parser = subparser.add_parser('init', help="check status")

    
    args = parser.parse_args()

    commands = {
        'init': init.check_git_config
    }

    if args.command in commands:
        commands[args.command]()
    else:
        parser.print_help()
        


if __name__ == "__main__":
    main()