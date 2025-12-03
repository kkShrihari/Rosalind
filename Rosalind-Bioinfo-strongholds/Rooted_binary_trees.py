class Rooted_binary_trees:
    """
    A class to compute the number of rooted binary trees with n labeled leaves,
    using the formula (2n − 3)!!  (double factorial), modulo 1,000,000.
    """
    print("\n")

    def __init__(self, input):
        """
        Parameters:
        input (int): Number of leaves (must be ≤ 1000).
        """
        self.n = input

    def RBT(self):
        """
        Computes the number of rooted binary trees using:
        (2n − 3)!! = product of all odd integers up to (2n − 3)

        Applies modulo 1,000,000 to each multiplication step.

        Returns:
        int: The total number of rooted binary trees modulo 1,000,000.
        """
        if self.n > 1000:
            raise ValueError("Enter input less than 1000")
        dob_fac_of = (2*self.n - 3)
        total_val = 1
        for i in range(1, dob_fac_of + 1):
            if i % 2 != 0:
                total_val = (total_val * i) % 1000000
        return total_val


input = 999
RBT1 = Rooted_binary_trees(input)
print(RBT1.RBT())
