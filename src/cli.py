import argparse
import sys
from colorama import init

import commands.init as initialize
import commands.status as status


def hell():
    print("hi")


def main():
    if len(sys.argv) < 2:
        print("Wrong input, please type --help for help!")
        sys.exit(1)

    parser = argparse.ArgumentParser(
        description="Simply check your pipeline with one command"
    )

    subparser = parser.add_subparsers(dest="command", help="available command")

    # commands definition
    init_parser = subparser.add_parser("init", help="check status")

    status_parser = subparser.add_parser(
        "status",
        help="check pipeline status",
    )
    status_parser.add_argument(
        "--all",
        action="store_true",
        help="get status of the last 100 pipelines",
    )
    status_parser.add_argument(
        "--jobs", action="store_true", help="include jobs in a pipeline"
    )

    args = parser.parse_args()

    commands = {
        "init": initialize.init_git_config,
        "status": status.check_status,
    }

    if args.command in commands:
        try:
            commands[args.command](args)
        except argparse.ArgumentError as e:
            print(e)
            raise SystemExit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    # Initialize colorama
    init(autoreset=True)

    main()
