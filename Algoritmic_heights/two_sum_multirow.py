def two_sum(input):
    """
    For each row of integers, checks whether any two numbers are negatives of each other.

    Parameters:
        input (str): Multiline string with dimensions and numbers.

    Returns:
        str: Formatted output showing index pairs or -1.
    """
    val_list = input.splitlines()
    k, n = map(int, val_list[0].split(" "))
    val_list.pop(0)

    val_list = [list(map(int, row.split())) for row in val_list]

    i = 0
    final = []
    temp1 = []
    while i != len(val_list):
        sub_list = [[-(i) for i in temp] for temp in val_list]
        mid_list = []
        for idx0, i0 in enumerate(val_list[i]):
            for idx1, i1 in enumerate(sub_list[i]):
                if int(i0) == i1:
                    mid_list.append(int(i0))
        mid_list.sort()
        mid_list = [i for i in mid_list if i > 0]

        if mid_list != []:
            temp1.append(val_list[i].index(int(mid_list[0])) + 1)
            temp1.append(val_list[i].index(-(int(mid_list[0]))) + 1)
            final.append(temp1)
        else:
            final.append([-1])
        temp1 = []
        i += 1

    result = ""
    for item in final:
        if len(item) == 1:
            result += str(item[0]) + "\n"
        else:
            result += " ".join(str(x) for x in item) + "\n"
    return result
