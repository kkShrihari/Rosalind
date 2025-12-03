class CharacterTableBuilder:
    """
    A class to construct a character table from a list of aligned DNA sequences.
    """

    def __init__(self, data):
        """
        Parameters:
        data (str): Multi-line string of equal-length sequences (no FASTA headers).
        """
        print("\n")
        self.input_data = data

    def Phy_gen_char(self):
        """
        Builds a character table by examining each column of the alignment:
        - Extracts each column across all sequences.
        - Converts the column into a binary string where the majority symbol = '1'
          and all other symbols = '0'.
        - Removes columns where all characters are identical.

        Returns:
        str: Character table, one binary string per line.
        """
        final_list = list(self.input_data.strip().splitlines())
        
        s, trans_list = "", []
        for i in range(len(final_list[0])):
            for i1 in range(len(final_list)):
                s += final_list[i1][i]
            trans_list.append(s)
            s = ""
        
        list_final = []
        for m in range(len(trans_list)):
            num = ""
            for n in range(len(trans_list[0])):
                value = trans_list[m][0]
                if trans_list[m][n] == value:
                    num += "1"
                else:
                    num += "0"
            list_final.append(num)

        sum1 = ""
        for i in range(len(list_final)):
            if len(set(trans_list[i])) == 1:
                continue
            else:
                sum1 += list_final[i] + "\n"
        return sum1


input_data = '''
ATGCTACC
CGTTTACC
ATTCGACC
AGTCTCCC
CGTCTATC
'''
CTB1 = CharacterTableBuilder(input_data)
print(CTB1.Phy_gen_char())
