class Transition_and_Transversions:
    """
    A class to compute the transition/transversion ratio between two DNA sequences
    provided in FASTA format.
    """

    def __init__(self, fasta_input):
        """
        Initializes the object with FASTA-formatted input.

        Parameters:
        fasta_input (str): Multi-line FASTA string containing exactly two sequences.
        """
        self.fasta_input = fasta_input

    def T_and_T(self):
        """
        Extracts two DNA sequences from FASTA input, counts the transitions and
        transversions between them, and returns their ratio.

        Returns:
        float: Transition/transversion ratio rounded to 11 decimals.
        """
        final_list, temp_list = [], []
        str_list = self.fasta_input.strip().splitlines()

        for line in str_list:
            if line.startswith(">"):
                if temp_list:
                    final_list.append("".join(temp_list))
                    temp_list = []
                continue
            temp_list.append(line)

        if temp_list:
            final_list.append("".join(temp_list))

        print(final_list)

        # Transition pairs: A ↔ G, C ↔ T
        # Transversion pairs: A ↔ C/T, G ↔ C/T

        transition = 0
        transversion = 0
        for i in range(len(final_list[0])):
            if final_list[0][i] == final_list[1][i]:
                continue
            elif (final_list[0][i] in "AG") and (final_list[1][i] in "AG"):
                transition += 1
            elif (final_list[0][i] in "TC") and (final_list[1][i] in "CT"):
                transition += 1
            elif (final_list[0][i] in "A") and (final_list[1][i] in "CT"):
                transversion += 1
            elif (final_list[0][i] in "G") and (final_list[1][i] in "CT"):
                transversion += 1
            elif (final_list[0][i] == "C") and (final_list[1][i] in "AG"):
                transversion += 1
            elif (final_list[0][i] == "T") and (final_list[1][i] in "AG"):
                transversion += 1
        
        Compute_ratio = transition / transversion
        return round(Compute_ratio, 11)


fasta_input = '''
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT
'''

TT1 = Transition_and_Transversions(fasta_input)
print(TT1.T_and_T())
