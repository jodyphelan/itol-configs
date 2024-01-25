import argparse
from . import colour_strip
from . import text_label
from . import binary_data

def cli():
    """Command-line interface for the itol_configs package."""
    parser = argparse.ArgumentParser(
        description="Generate iTOL configuration files",
        prog="itol_configs"
    )

    subparsers = parser.add_subparsers(
        title="subcommands",
        description="Different types of configuration files",
        help="sub-command help"
    )

    colour_strip.register_subparser(subparsers)
    text_label.register_subparser(subparsers)
    binary_data.register_subparser(subparsers)
    
    args = parser.parse_args()
    if hasattr(args,"func"):
        args.func(args)
    else:
        parser.print_help()
