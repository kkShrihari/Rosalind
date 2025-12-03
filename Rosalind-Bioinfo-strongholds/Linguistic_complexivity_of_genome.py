# Linguistic Complexity of a Genome
def LCOG(input):
    """
    Computes the Linguistic Complexity of a DNA string.

    Linguistic Complexity = (number of observed distinct substrings) /
                            (number of possible distinct substrings)

    Parameters:
    input (str): DNA sequence consisting of A, T, G, C.

    Returns:
    float: Linguistic complexity value between 0 and 1.
    """

    data = input
    length = len(data)

    list2, set1 = [], set()
    for i in range(1, length + 1):               # substring lengths
        for x in range(0, length):
            substring = data[x:x + i]
            if len(substring) == i:
                set1.add(substring)
        list2.append(set1)
        set1 = set()
    print(list2)

    # Count observed distinct substrings
    sub_len_list = []
    for i in list2:
        x = len(i)
        sub_len_list.append(x)
    num = sum(sub_len_list)

    # Count total possible substrings
    denom_list = []
    for k in range(1, length + 1):
        possible = min(4**k, length - k + 1)
        denom_list.append(possible)
    denom = sum(denom_list)

    return (num / denom)


input = "ATTTGGATT"
print(LCOG(input))
