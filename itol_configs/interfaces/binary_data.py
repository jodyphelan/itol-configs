from .base_interface import ConfigWriterMatrix
from typing import Optional, Dict, List

template = """DATASET_BINARY
SEPARATOR TAB
DATASET_LABEL\t%(dataset_label)s
COLOR\t#ff0000

SHOW_LABELS\t1
FIELD_SHAPES\t%(field_shapes)s
FIELD_COLORS\t%(field_colours)s
FIELD_LABELS\t%(field_labels)s

DATA
"""

class BinaryConfigWriter(ConfigWriterMatrix):    
    def __init__(self, data: Dict[str,dict], label: str, colour_lookup: Optional[dict] = None, shape: int = 2,):
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
        shape : int
            Shape of the field.
        
        Returns
        -------
        None
        """
        super().__init__(data,label,colour_lookup)
        self.config["field_shapes"] = "\t".join([str(shape) for _ in self.colour_lookup])
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
        with open(outfile,"w") as O:
            O.write(template % self.config)
            for index, values in self.data.items():
                binary_data = "\t".join([str(x) for x in values.values()])
                O.write("%s\t%s\n" % (index,binary_data))
