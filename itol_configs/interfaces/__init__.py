from typing import Optional
from .base_interface import ConfigWriter
from .colour_strip import ColourStripConfigWriter
from .text_label import TextConfigWriter


def get_config_writer(config_type: str, data: dict, label: str, colour_lookup: Optional[dict] = None) -> ConfigWriter:
    """
    Get the appropriate ConfigWriter object.
    
    Parameters
    ----------
    config_type : str
        Type of configuration file to write.
    
    Returns
    -------
    ConfigWriter
        ConfigWriter object.
    """
    if config_type=="colour_strip":
        return ColourStripConfigWriter(data,label,colour_lookup)
    elif config_type=="text":
        return TextConfigWriter(data,label,colour_lookup)
    else:
        raise ValueError(f"Unknown configuration type: {config_type}")