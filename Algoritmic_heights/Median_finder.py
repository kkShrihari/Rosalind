def find_median(input):
    """
    Finds the median from a given list of numbers.

    Parameters:
        input (str): Multiline string with list length, numbers, and index.

    Returns:
        int: The median value at the given position.
    """
    data = input.splitlines()
    val_list = [int(i) for i in data[1].split()]
    val_list.sort()
    med_no = data[2]
    return val_list[int(med_no) - 1]
