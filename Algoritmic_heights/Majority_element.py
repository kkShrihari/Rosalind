def Majority_element(input):
    """
    Determines majority element (> n/2 occurrences) for each list.

    Parameters:
        input (str): Multiline string with row count, size, and lists.

    Returns:
        str: Majority element or -1 for each list.
    """
    data = input.splitlines()
    no, size = map(int, data[0].split())
    data_list = data[1:no+1]
    data_list = [x.split(" ") for x in data_list]
    
    i = 0
    dict1, list1 = {}, []
    while i != no:
        for x in data_list[i]:
            count = data_list[i].count(x)
            dict1[int(x)] = count
        list1.append(dict1.copy())
        dict1.clear()
        i += 1

    result = ""
    for y in list1:
        checker = int(size)//2
        flag = False
        for x in y:
            if y[x] > checker:
                result += str(x) + " "
                flag = True
        if not flag:
            result += "-1 "
    return result
