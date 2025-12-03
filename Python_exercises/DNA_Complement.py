def DNA_complement(DNA_sequence):
    """
    Computes the reverse complement of a DNA sequence.
    Steps:
    - Reverse sequence
    - Convert A → a and C → c (temporary lowercasing)
    - Replace nucleotides to form complement
    """
    Reverse_DNA_Sequence = DNA_sequence[::-1]
    Count_1 = ""
    for nucleotide_A in Reverse_DNA_Sequence:
        if nucleotide_A == "A":
            Count_1 += nucleotide_A.lower()
        else:
            Count_1 += nucleotide_A
    Count_2 = ""
    for nucleotide_C in Count_1:
        if nucleotide_C == "C":
            Count_2 += nucleotide_C.lower()
        else:
            Count_2 += nucleotide_C
    A = Count_2.replace("G","A")
    G = A.replace("a","G")
    T = G.replace("T","C")
    C = T.replace("c","T")
    print(f"The Given sequence is:{DNA_sequence}")
    print(f"The Reverse complement is:{C}")

DNA_sequence = "ATGCATGCATGC"
DNA_complement(DNA_sequence)
