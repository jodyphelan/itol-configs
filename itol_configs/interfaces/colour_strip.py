from .base_interface import ConfigWriter

template = """DATASET_COLORSTRIP
SEPARATOR TAB
DATASET_LABEL\t%(dataset_label)s
COLOR\t#ff0000

LEGEND_TITLE\t%(legend_title)s
LEGEND_SHAPES\t%(legend_shapes)s
LEGEND_LABELS\t%(legend_labels)s
LEGEND_COLORS\t%(legend_colours)s

DATA
"""

class ColourStripConfigWriter(ConfigWriter):
    def write(self, outfile: str) -> None:
        """
        Parse the data to be coloured.
        
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
            for index, value in self.data.items():
                O.write("%s\t%s\n" % (index,self.colour_lookup[value]))
