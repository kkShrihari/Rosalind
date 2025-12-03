class Amino_acid_finder:
    """
    A class to determine the amino acid sequence from a list of increasing
    mass values by computing pairwise differences and matching them to
    known monoisotopic amino acid masses.
    """

    aa_mass = {
        'A': 71.0371,  # Alanine
        'C': 103.0092, # Cysteine
        'D': 115.0269, # Aspartic Acid
        'E': 129.0426, # Glutamic Acid
        'F': 147.0684, # Phenylalanine
        'G': 57.0215,  # Glycine
        'H': 137.0589, # Histidine
        'I': 113.0841, # Isoleucine
        'K': 128.0949, # Lysine
        'L': 113.0841, # Leucine
        'M': 131.0405, # Methionine
        'N': 114.0429, # Asparagine
        'P': 97.0528,  # Proline
        'Q': 128.0586, # Glutamine
        'R': 156.1011, # Arginine
        'S': 87.0320,  # Serine
        'T': 101.0477, # Threonine
        'V': 99.0684,  # Valine
        'W': 186.0793, # Tryptophan
        'Y': 163.0633  # Tyrosine
    }

    def __init__(self, input_data):
        """
        Parameters:
        input_data (str): Multi-line string of increasing cumulative mass values.
        """
        self.input_data = input_data

    def rev_calc(self):
        """
        Computes the amino acid sequence by taking differences of adjacent masses
        and mapping those differences to known amino acid masses.

        Returns:
        str: The reconstructed amino acid sequence.
        """
        filter_list = list(self.input_data.strip().splitlines())
        filter_list = [float(i) for i in filter_list]

        clean_list = []
        for i in range(len(filter_list) - 1):
            value = round((filter_list[i+1]) - (filter_list[i]), 4)
            clean_list.append(value)
       
        no = ""
        for i in range(len(clean_list)):
            for x, y in self.aa_mass.items():
                if clean_list[i] == y:
                    no += x
        return no 
    


input_data = ''' 
3524.8542
3710.9335
3841.974
3970.0326
4057.0646
'''

AAF =  Amino_acid_finder(input_data)
print(AAF.rev_calc())
