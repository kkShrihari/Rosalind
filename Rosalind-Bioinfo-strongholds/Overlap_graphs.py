class Overlap_graphs:
    """
    A class to construct overlap graphs from FASTA sequences.
    It finds directed edges between sequence labels when the
    suffix of length k in one sequence matches the prefix of
    length k in another sequence.
    """
    def __init__(self, sequence, k):
        """
        Initializes the overlap graph generator.

        Parameters:
        sequence (str): FASTA formatted string.
        k (int): Length of prefix/suffix to compare.
        """
        self.k = k
        self.sequence = sequence

    def Node_match(self):
        """
        Identifies all pairs of sequences where the suffix of
        length k in one matches the prefix of length k in another.
        
        Returns:
        str: A list of edges in the format "node1 node2".
        """
        cropped_list = list(self.sequence.strip().splitlines())
        print(cropped_list)
        final = ""
        for i in range(1, len(cropped_list), 2):
            for i1 in range(1, len(cropped_list), 2):
                if (cropped_list[i][-(self.k):] == cropped_list[i1][0:(self.k)]) and (i != i1):
                   final = final + cropped_list[i-1][1:] + " " + cropped_list[i1-1][1:] + "\n"
        return final


fasta_input ="""
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
"""
OG1 = Overlap_graphs(fasta_input, 3)
print(OG1.Node_match())
