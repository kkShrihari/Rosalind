def degree_array(data_arr):
    """
    Computes the degree of each vertex in an undirected graph.

    Parameters:
        data_arr (str): Multiline string describing edge list.

    Returns:
        list[int]: Degrees of vertices (1..n).
    """
    seq = data_arr.split()
    edges_count = int(seq[1])
    max_val = int(max(seq[2:]))
    num_seq = [int(i) for i in seq]

    final_list = []
    for x in range(edges_count):
        final_list.append(num_seq[2*x+2 : 2*x+4])

    end_list = []
    for i in range(1, max_val + 1):
        no = 0
        for n1 in final_list:
            for n2 in n1:
                if i == n2:
                    no += 1
        end_list.append(no)
    return end_list
