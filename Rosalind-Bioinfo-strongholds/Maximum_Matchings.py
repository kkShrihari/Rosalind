class Maximum_Matchings:
    """
    A class to compute the number of maximum matchings in an RNA string
    based on valid base-pairing rules (A–U and G–C).
    """

    def __init__(self, fasta_input):
        """
        Parameters:
        fasta_input (str): FASTA-formatted RNA sequence input.
        """
        print("\n")
        self.fasta_input = fasta_input

    def factorial_(self, val):
        """
        Computes factorial of an integer.

        Parameters:
        val (int): The integer to compute factorial for.

        Returns:
        int: val!
        """
        sum = 1
        for i in range(1, val + 1):
            sum *= i
        return sum
    
    def RNA_SS(self):
        """
        Extracts the RNA sequence, counts occurrences of A, U, G, and C,
        and computes the number of perfect matchings using:
        
        matches(A,U) * matches(G,C)

        Returns:
        int: Number of possible maximum matchings.
        """
        final_list = []
        list1 = list(self.fasta_input.strip().splitlines())
        for i in list1:
            if not i.startswith(">"):
                final_list.append(i)
        
        # A - U and G - C
        a, u, g, c = 0, 0, 0, 0
        for i in range(len(final_list)):
            a = final_list[i].count("A")
            u = final_list[i].count("U")
            g = final_list[i].count("G")
            c = final_list[i].count("C")

            maximum1 = max(a, u)
            minimum1 = min(a, u)

            maximum2 = max(g, c)
            minimum2 = min(g, c)

            matches_au = self.factorial_(maximum1) / self.factorial_(maximum1 - minimum1)
            matches_gc = self.factorial_(maximum2) / self.factorial_(maximum2 - minimum2)

            possibilities = matches_au * matches_gc
            return int(possibilities)
            

input_data = '''
>Rosalind_92
AUGCUUC
'''
MM1 = Maximum_Matchings(input_data)
print(MM1.RNA_SS())
