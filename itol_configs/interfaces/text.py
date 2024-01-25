from .base_interface import ConfigWriter

template = """DATASET_TEXT
SEPARATOR TAB
DATASET_LABEL\t%(dataset_label)s
COLOR\t#ff0000

LEGEND_TITLE\t%(legend_title)s

DATA
"""

class TextConfigWriter(ConfigWriter):
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
                O.write("%s\t%s\t-1\t%s\tnormal\t1\t0\n" % (index,self.data[index],self.colour_lookup[value]))
