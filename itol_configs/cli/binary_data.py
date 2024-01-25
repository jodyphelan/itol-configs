import argparse
from ..interfaces.binary_data import BinaryConfigWriter
from ..utils import load_binary_matrix_data
from ..colour import load_colour_conf

def run(args: argparse.Namespace) -> None:
    """
    Run the colour_strip subcommand
    
    Parameters
    ----------
    args : argparse.Namespace
        Arguments from the command-line
    """
    
    if args.colour_conf:
        colour_conf = load_colour_conf(args.colour_conf)
    else:
        colour_conf = {}
    
    
    data = load_binary_matrix_data(args.input,args.id)
    writer = BinaryConfigWriter(data,args.output,colour_conf,shape=args.symbol)
    writer.write(args.output + ".txt")


def register_subparser(subparsers: argparse._SubParsersAction) -> None:
    """
    Register subparser for the itol_configs package
    
    Parameters
    ----------
    subparser : argparse.ArgumentParser
        Subparser object for the itol_configs package
    """
    subparser = subparsers.add_parser('binary_data', help='Generate a text label configuration file')
    subparser.add_argument(
        "--input",
        help="Input file containing a csv file with sequence metadata",
        type=str,
        required=True
    )
    subparser.add_argument(
        "--output",
        help="Output file name for the iTOL configuration file",
        type=str,
        required=True
    )
    subparser.add_argument(
        "--id",
        help="Column name matching the sequence IDs used in the tree",
        type=str,
        default="id"
    )
    subparser.add_argument(
        "--colour-conf",
        help="Colour configuration file",
        type=str,
        default=None
    )
    subparser.add_argument(
        "--symbol",
        help="The symbol to use for the binary data (1: square, 2: circle, 3: star, 4: right triangle, 5: left triangle, 6: checkmark)",
        type=int,
        choices = [1,2,3,4,5,6],
        default=2
    )
    
    subparser.set_defaults(func=run)
