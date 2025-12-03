from itertools import count

def is_vampire(n):
    """
    Checks whether a number is a vampire number.
    A vampire number has an even number of digits and can be factored into
    two numbers ("fangs") whose digits form the same multiset as the original number.

    Parameters:
        n (int): Input integer

    Returns:
        int or bool: n if vampire, False otherwise.
    """
    list_new = []
    z1 = str(n)
    z2 = len(z1)
    z3 = int(z2/2)
    if z2 % 2 == 0:
        z4 = 10**(z3-1)
        z5 = 10**(z3-1)
        z6 = (-1 + 10**(z3))

        value = range(z4, z6+1)
        value1 = range(z5, z6+1)

        for x in value:
            for y in value1:
                vampire_number = x * y
                if vampire_number == n:
                    n1 = str(n)
                    n2 = list(n1)
                    x2 = list(str(x))
                    y2 = list(str(y))
                    x2.extend(y2)
                    if sorted(x2) == sorted(n2):
                        if int(x2[-1]) != 0 and int(y2[-1]) != 0:
                            return n
        return False
    else:
        return False


def vampire_generator():
    """
    Generates vampire numbers starting from 1259 using an infinite generator.

    Yields:
        int: next vampire number
    """
    for x in count(1259):
        if is_vampire(x):
            if x is not None:
                yield x
