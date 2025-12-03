class Isolating_Symbols_in_Alignments:
    """
    A class to count matches, mismatches, and gaps between two aligned sequences.
    """

    def __init__(self, fasta_input):
        """
        Initializes the class with FASTA input containing exactly two aligned sequences.

        Parameters:
        fasta_input (str): FASTA-formatted string with two sequences.
        """
        print("\n")
        self.fasta_input = fasta_input
    
    def ISA(self):
        """
        Computes:
        - Matches (+1)
        - Mismatches (−1)
        - Gaps (−1)

        Prints the sequences and their combined scoring component count.
        """
        '''
        Match = +1
        Mismatch = -1
        Gap = -1
        '''
        final_list = []
        filter_list = list(self.fasta_input.strip().splitlines())
        for i in filter_list:
            if not i.startswith(">"):
                final_list.append(i)
        print(final_list)

        if len(final_list) != 2:
            raise ValueError("enter 2 strings not less not more")
        if len(final_list[0]) != len(final_list[1]):
            raise ValueError("2 sequence must be in same sequence")
        
        m, mm, g = 0, 0, 0
        for i1 in range(len(final_list[0])):
            if final_list[0][i1] == final_list[1][i1]:
                m += 1
            if final_list[0][i1] == final_list[1][i1]:
                mm += 1
            if (final_list[0][i1] == "-") or (final_list[1][i1] == "-"): 
                g += 1

        sum = m + mm + g
        print(sum)



input  = '''
>Rosalind_35
ATAGATA
>Rosalind_5
ACAGGTA
'''
ISA1 = Isolating_Symbols_in_Alignments(input)
ISA1.ISA()
