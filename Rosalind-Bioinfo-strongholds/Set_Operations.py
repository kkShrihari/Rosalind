class SetOperations:
    """
    A class to perform basic set operations on two sets within a universal set.
    """

    def __init__(self, m, n, o):
        """
        Initializes the set operator.

        Parameters:
        m (int): Size of the universal set (1 to m).
        n (set): First input set.
        o (set): Second input set.
        """
        self.m = m
        self.set1 = n
        self.set2 = o

    def set_op(self):
        """
        Computes and prints:
        - Union of the two sets
        - Intersection of the two sets
        - Difference (set1 - set2)
        - Difference (set2 - set1)
        - Complement of set1 relative to universal set
        - Complement of set2 relative to universal set
        """
        set_base = set()
        for i in range(1, (self.m + 1)):
            set_base.add(int(i))

        set_union = self.set1.union(self.set2)
        print(set_union)

        set_intersection = self.set1.intersection(self.set2)
        print(set_intersection)

        difference1 = self.set1.difference(self.set2)
        print(difference1)

        difference2 = self.set2.difference(self.set1)
        print(difference2)

        complement1 = set_base - self.set1
        print(complement1)

        complement2 = set_base - self.set2
        print(complement2)


x = 10
y = {1, 2, 3, 4, 5}
z = {2, 8, 5, 10}
SO = SetOperations(x, y, z)
SO.set_op()
