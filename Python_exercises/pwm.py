# TASK_2
def pwm(filename):
    """
    Constructs a Position Weight Matrix (PWM) from sequences in a file.
    
    Parameters:
        filename (str): file containing equal-length DNA sequences

    Returns:
        list[list[int]]: 4xN PWM matrix in A,C,G,T order
    """
    with open(filename,'r') as seq:
        seq_data = seq.readlines()

    clean_seq_data = [x.strip() for x in seq_data]
    n = len(clean_seq_data[0])
    pwm = [[0]*n for count in range(4)]
    ref_index = {"A":0, "C":1, "G":2, "T":3}

    for sequence in clean_seq_data:
        for x, y in enumerate(sequence):
            pwm[ref_index[y]][x] += 1

    return pwm
