# TASK_1
def read_config(stacks):
    """
    Reads a configuration file describing parcel stacks and movement instructions.

    File format expected:
    - Upper section: stack layout using bracketed boxes (e.g., [A] [B] ...)
    - Lower section: move commands (e.g., 'move 3 from 1 to 2')

    Returns:
        tuple:
            ref_dict (dict): {stack_number: [box1, box2, ...]}
            moving_conditions (list): list of movement instructions as tuples:
                                      (no_parcels, source_stack, destination_stack)
    """
    with open(stacks,'r') as orders:
        rows = orders.readlines()

    read_move = False
    ref_dict = {}
    moving_conditions = []
    stackinglines, movinglines = [], []

    # Reading stack and move sections
    for row in rows:
        row = row.rstrip()
        if row.startswith("m"):
            read_move = True
        elif not read_move:
            stackinglines.append(row)
        else:
            movinglines.append(row)
    
    # Parsing stack section
    number = len(stackinglines[-1].split())
    for no in range(number):
        ref_dict[no+1] = []

    for row in reversed(stackinglines[:-1]):
        id = 1
        for val in range(0, len(row), 4):
            boxes = row[val:val+3].strip(' []')
            if boxes:
                ref_dict[id].append(boxes)
            id += 1

    # Parsing movement instructions
    for row in rows:
        if row.startswith('m'):
            components = row.strip().split()
            no_parcels = int(components[1])
            current_holding = int(components[3])
            new_stack = int(components[5])
            moving_conditions.append((no_parcels, current_holding, new_stack))

    return ref_dict, moving_conditions


def rearrange_parcels(dict_1, answer):
    """
    Rearranges parcels in stacks based on movement instructions.

    Parameters:
        dict_1 (dict): stack dictionary containing lists of boxes
        answer (list): movement instructions in form (count, from, to)

    Returns:
        str: A string formed from the top box of each stack after all moves.
    """
    moving = answer
    stack_dict_idx = dict_1

    for x, y, z in moving:
        for val in range(x):
            if stack_dict_idx[y]:
                parcels = stack_dict_idx[y].pop()
                stack_dict_idx[z].append(parcels)

    upper_boxes = [num[-1] for num in stack_dict_idx.values() if num]
    outcome = ''.join(upper_boxes)
    return outcome


