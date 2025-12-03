 import time
 start = time.time()

def BWT(data):
    """
    Computes the Burrows-Wheeler Transform (BWT) of the given input string.

    The function generates all cyclic rotations of the input, sorts them
    lexicographically, and returns the last column of the sorted rotation matrix,
    which is the BWT result.

    Parameters:
        data (str): The input string ending with the terminator symbol ('$').

    Returns:
        str: The Burrows-Wheeler transformed string.
    """

    list1 = []
    for i in range(len(data)):
        data = data[1:] + data[0]
        list1.append(data)
    print(list1)

    list1.sort()
    
    result_str = ""
    for i in range(len(list1[0])):
        result_str += str(list1[i][-1])
    
    return result_str

input = "GCGTGCCTGGTCA$"
print(BWT(input))

end = time.time()
print("time taken:", end - start)
