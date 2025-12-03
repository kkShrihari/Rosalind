def get_treasure(filename):
    """
    Solves the 'mixing' puzzle by rearranging integers according
    to their own values modulo (n - 1). Used to locate the 'treasure room'.

    Process:
        - Read one integer per line.
        - Move each number forward by its own value (cyclic).
        - Find index of value 0.
        - Sum the numbers 1000, 2000, 3000 positions after 0.

    Parameters:
        filename (str): File containing one integer per line.

    Returns:
        int: The computed treasure room number.
    """
    with open(filename, 'r') as list_numbers:
        list_of_int = [int(num.strip()) for num in list_numbers]
    
    length_of_list = len(list_of_int)
    original_list_of_int = list_of_int[:]
 
    for val in original_list_of_int:
        idx = list_of_int.index(val)
        list_of_int.pop(idx)
        new_idx = (idx + val) % (length_of_list - 1)
        list_of_int.insert(new_idx, val)

    idx_0 = list_of_int.index(0)
    the_room_no = sum(list_of_int[(idx_0 + y * 1000) % length_of_list] for y in range(1, 4))
    return the_room_no
