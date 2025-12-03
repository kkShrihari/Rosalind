def insert_sort(data):
    """
    Computes the number of shifts required to sort an array using insertion sort.

    Parameters:
        data (str): Multiline string containing length and values.

    Returns:
        int: The number of shifts performed.
    """
    data = data.splitlines()
    val_list = [int(i) for i in data[1].split()]

    shift = 0
    sort_list = sorted(val_list)

    while val_list != sort_list:
        for i in range(len(val_list)-1):
            if val_list[i+1] < val_list[i]:
                val_list[i], val_list[i+1] = val_list[i+1], val_list[i]
                shift += 1
    return shift
