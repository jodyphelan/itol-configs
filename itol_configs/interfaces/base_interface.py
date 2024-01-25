from abc import ABC, abstractmethod
from typing import Optional
from ..colour import get_colour_lookup

class ConfigWriter(ABC):
    """
    Abstract base class for iTOL configuration file writers.
    """
    def __init__(self, data: dict, label: str, colour_lookup: Optional[dict] = None):
        """
        Initialise a ConfigWriter object.
        
        Parameters
        ----------
        data : dict
            Dictionary containing the values to be coloured.
        label : str
            Label for the colour strip.
        colour_lookup : Optional[dict]
            Dictionary of colours for each unique value in the data.
            If not provided, it will be generated.
        
        Returns
        -------
        None
        """
        self.data = data
        self.label = label
        if colour_lookup is None:
            colour_lookup = get_colour_lookup(data.values())
        self.colour_lookup = colour_lookup
        self.config = {
            "dataset_label":self.label,
            "legend_title":self.label,
            "legend_shapes":"\t".join(["1" for _ in self.colour_lookup]),
            "legend_labels":"\t".join([str(x) for x in self.colour_lookup]),
            "legend_colours":"\t".join([self.colour_lookup[x] for x in self.colour_lookup])
        }

    @abstractmethod
    def write(self, outfile: str) -> None:
        """
        Write the iTOL configuration file.
        
        Parameters
        ----------
        outfile : str
            Output file name.
        
        Returns
        -------
        None
        """
        raise NotImplementedError
    