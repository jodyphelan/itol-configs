"""This package contains functions to generate iTOL configuration files."""
import argparse
import csv
from typing import Dict
from .interfaces import get_config_writer, interface_types
from .colour import load_colour_conf

__version__ = "0.1.0"




def sanitise(x: str) -> str:
    """
    Sanitise a string for use in a file name.
    
    Parameters
    ----------
    x : str
        String to be sanitised.
    
    Returns
    -------
    str
        Sanitised string.

    Examples
    --------
    >>> sanitise("Hello World")
    "Hello_World"
    >>> sanitise("Hello/World")
    "Hello_World"
    >>> sanitise("Hello (World)")
    "Hello_World"
    """
    return x.replace(" ","_").replace("/","_").replace("(","").replace(")","")

def load_data(input_file: str, id_column: str) -> Dict[str,dict]:
    """
    Load data from a csv file.
    
    Parameters
    ----------
    input_file : str
        Input file name.
    id_column : str
        Column name matching the sequence IDs used in the tree.
    
    Returns
    -------
    dict
        Dictionary of dictionaries for each column in the csv file.
    """
    data = {}
    rows = []
    for row in csv.DictReader(open(input_file,encoding="utf-8-sig")):
        rows.append(row)
    columns = list(rows[0].keys())
    for column in columns:
        if column != id_column:
            data[column] = {row[id_column]:row[column] for row in rows}
    return data


def main(args):
    """
    Main function for the itol_configs package
    
    Parameters
    ----------
    args : argparse.Namespace
        Namespace object containing the command-line arguments.
    
    Returns
    -------
    None
    """
    data = load_data(args.input,args.id)
    if args.colour_conf:
        colour_conf = load_colour_conf(args.colour_conf)
    else:
        colour_conf = {}

    for column in data:
        output_file = f"{args.output}.{sanitise(column)}.txt"
        writer = get_config_writer(args.type,data[column],column,colour_conf.get(column,None))
        writer.write(output_file)
        


    

def cli():
    """Command-line interface for the itol_configs package."""
    parser = argparse.ArgumentParser(
        description="Generate iTOL configuration files",
        prog="itol_configs"
    )
    parser.add_argument(
        "--input",
        help="Input file containing a csv file with sequence metadata",
        type=str,
        required=True
    )
    parser.add_argument(
        "--output",
        help="Output file name for the iTOL configuration file",
        type=str,
        required=True
    )
    parser.add_argument(
        "--id",
        help="Column name matching the sequence IDs used in the tree",
        type=str,
        default="id"
    )
    parser.add_argument(
        "--type",
        help="Type of iTOL configuration file to generate",
        type=str,
        choices=interface_types.keys(),
        required=True
    )
    parser.add_argument(
        "--colour-conf",
        help="Colour configuration file",
        type=str,
        default=None
    )
    
    args = parser.parse_args()
    main(args)