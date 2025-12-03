def Fibonacci_no(no, n=0):
    """
    Computes the nth Fibonacci number using iterative list building.

    Parameters:
        no (int): The index of the Fibonacci number to compute.
        n  (int): Internal counter used during sequence building (default 0).

    Returns:
        int: The Fibonacci number at position `no`.
    """
    Output_list = []
    if no == 0:
        return 0
    if no == 1:
        return 1

    if n == 0:
        Output_list.append(n)
        n += 1
    if n == 1:
        Output_list.append(n)
        n += 1
    if n != no:
        for i in range(no - 1):
            val = Output_list[-1] + Output_list[-2]
            Output_list.append(val)
    return Output_list[-1]

