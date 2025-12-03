class Common_Ancestor:
    """
    A class to compute the consensus sequence and profile matrix
    from multiple DNA sequences provided in FASTA format.
    """
    def __init__(self, fasta_seq):
        self.fasta_seq = fasta_seq

    def Consensus_seq_check(self):
        """
        Generates the consensus sequence and profile matrix by
        counting nucleotide frequencies column-wise across all sequences.
        """
        seq_list1,seq_list = [],[]
        seq_list1 = self.fasta_seq.strip().splitlines()
        for i in seq_list1:
            if not i.startswith(">"):
                seq_list.append(i)
        for i in seq_list:        
            if len(seq_list[0]) == len(i) and len(i) < 1000:
               continue
            else:
                print("May be non-equal seq length or more than 10 seq or seq length more than 1k")

        reversed_list = []
        count = 0
        for it in range(len(seq_list[0])): 
            if count > len(seq_list):
                break
            col_string = ""
            for i in range(len(seq_list)):  
                col_string += seq_list[i][count]
            reversed_list.append(col_string)
            count += 1
        
        concensus_seq = ""
        a_string,c_string,g_string,t_string = "A:","C:","G:","T:"
        for i in reversed_list:
            a = i.count("A")
            t = i.count("T")
            g = i.count("G")
            c = i.count("C")
            
            a_string = a_string + " " + str(a)
            c_string = c_string + " " + str(c)
            g_string = g_string + " " + str(g)
            t_string = t_string + " " + str(t)
            
            sum = str(a)+str(c)+str(g)+str(t)
            maximum = max(sum)
            pos = sum.index(maximum)

            map_dict = {0:"A",1:"C",2:"G",3:"T"}
            for i in map_dict:
                if i == pos:
                    concensus_seq += map_dict[pos]
        print("\nThe concensus sequence and the profile matrix is:")
        return (
    concensus_seq + "\n" +   # consensus sequence on its own line
    a_string + "\n" +
    c_string + "\n" +
    g_string + "\n" +
    t_string
    )

fasta_input = """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
"""

sequences = Common_Ancestor(fasta_input)
print(sequences.Consensus_seq_check())
