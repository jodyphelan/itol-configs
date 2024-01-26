import tomli

def get_palette(num_items: int) -> list:
    """
    Generate a colour palette for a given number of items.
    
    Parameters
    ----------
    num_items : int
        Number of items to generate a palette for.
    
    Returns
    -------
    list
        List of colours for each item.
    """
    palette = {
        1:["#000000"],
        2:["#1b9e77","#7570b3"],
        3:['#1B9E77', '#D95F02', '#7570B3'],
        4:['#1B9E77', '#D95F02', '#7570B3', '#E7298A'],
        5:['#1B9E77', '#D95F02', '#7570B3', '#E7298A', '#66A61E'],
        6:['#1B9E77', '#D95F02', '#7570B3', '#E7298A', '#66A61E', '#E6AB02'],
        7:['#1B9E77', '#D95F02', '#7570B3', '#E7298A', '#66A61E', '#E6AB02', '#A6761D'],
        8:['#1B9E77', '#D95F02', '#7570B3', '#E7298A', '#66A61E', '#E6AB02', '#A6761D', '#666666'],
        9:['#A6CEE3', '#1F78B4', '#B2DF8A', '#33A02C', '#FB9A99', '#E31A1C', '#FDBF6F', '#FF7F00', '#CAB2D6'],
        10:['#A6CEE3', '#1F78B4', '#B2DF8A', '#33A02C', '#FB9A99', '#E31A1C', '#FDBF6F', '#FF7F00', '#CAB2D6', '#6A3D9A'],
        11:['#A6CEE3', '#1F78B4', '#B2DF8A', '#33A02C', '#FB9A99', '#E31A1C', '#FDBF6F', '#FF7F00', '#CAB2D6', '#6A3D9A', '#FFFF99'],
        12:['#A6CEE3', '#1F78B4', '#B2DF8A', '#33A02C', '#FB9A99', '#E31A1C', '#FDBF6F', '#FF7F00', '#CAB2D6', '#6A3D9A', '#FFFF99', '#B15928']
    }
    colours = palette.get(num_items,["black" for _ in range(num_items)])
    return colours

def get_colour_lookup(data: dict) -> dict:
    """
    Generate a dictionary of colours for each unique value in a dictionary.
    
    Parameters
    ----------
    data : dict
        Data containing the values to be coloured.
    
    Returns
    -------
    dict
        Dictionary of colours for each unique value in the dictionary.
    """
    unique_values = sorted(list(set(data)))
    num_unique_values = len(unique_values)
    palette = get_palette(num_unique_values)
    colour_lookup = {unique_values[i]:palette[i] for i in range(num_unique_values)}
    return colour_lookup

def load_colour_conf(tomlfile: str):
    """
    Load a colour configuration file.
    
    Parameters
    ----------
    tomlfile : str
        TOML file containing the colour configuration.
    
    Returns
    -------
    dict
        Dictionary of colours for each unique value in the dictionary.
    """
    colour_conf = tomli.load(open(tomlfile,'rb'))
    return colour_conf