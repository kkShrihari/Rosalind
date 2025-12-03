class Protein_mass:
    """
    A class to compute the total monoisotopic mass of a protein sequence
    using the standard protein mass table.
    """
    def __init__ (self, sequence):
        self.sequence = sequence

    def Mass_calculator(self):
        """
        Calculates the total mass of the protein by summing
        the monoisotopic masses of its amino acids.

        Returns:
        float: Total protein mass rounded to three decimals.
        """
        protein_mass_table = {
            'A': 71.03711,
            'C': 103.00919,
            'D': 115.02694,
            'E': 129.04259,
            'F': 147.06841,
            'G': 57.02146,
            'H': 137.05891,
            'I': 113.08406,
            'K': 128.09496,
            'L': 113.08406,
            'M': 131.04049,
            'N': 114.04293,
            'P': 97.05276,
            'Q': 128.05858,
            'R': 156.10111,
            'S': 87.03203,
            'T': 101.04768,
            'V': 99.06841,
            'W': 186.07931,
            'Y': 163.06333
        }
        sum1 = 0
        for i in range(len(self.sequence)):
            if self.sequence[i] in protein_mass_table:
                sum1 += protein_mass_table[self.sequence[i]]
        print("\n")
        return round(sum1, 3)


sequence = "SKADYEK"
PM1 = Protein_mass(sequence)
print(PM1.Mass_calculator())
