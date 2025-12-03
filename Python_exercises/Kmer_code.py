def Kmer_code(kmer):
    """
    Converts a k-mer into an integer using a 2-bit encoding scheme:
    A = 00, C = 01, G = 10, T = 11
    Uses bit shifting to generate a unique numeric code.
    """
    value = 0
    for x in kmer:
        value = value << 2
        if x == "G":
           value |= 2
        elif x == "T":
           value |= 3
        elif x == "C":
            value |= 1   
    return value

print(Kmer_code("ATGC"))
