class Shared_motif:
    """
    A class intended to find the longest common substring (shared motif)
    among multiple DNA sequences provided in FASTA format.
    """
    def __init__ (self, sequence):
        self.sequence = sequence

    def Max_substring(self):
        filtered_list = []
        lines = list(self.sequence.strip().splitlines())
        for i in lines:
            if not i.startswith(">"):
                filtered_list.append(i)
        if len(filtered_list) < 100:
            for i in range(len(filtered_list)):
                if (len(filtered_list[i]) <= 1000):
                    continue
        print(filtered_list)

        for i in range(len(filtered_list)):
            
            for n in range(len(filtered_list)):
            
                if i != n:
                    if filtered_list[i][]
                    


fasta_input = """
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
"""
SM1 = Shared_motif(fasta_input)
SM1.Max_substring()
