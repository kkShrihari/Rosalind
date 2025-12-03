class Rabbit_recurrence:
    """
    Computes the number of rabbit pairs after m months in a modified
    Fibonacci-style recurrence where each reproduction-age pair produces
    k new pairs per month.

    Parameters:
    m (int): Number of months.
    k (int): Number of rabbit pairs produced by each reproductive pair per month.

    Recurrence:
        F(n) = F(n-1) + k * F(n-2)
    """

    def __init__(self, m, k):
        self.m = m
        self.k = k

    def Rabbit_rec(self):
        """
        Calculates the number of rabbit pairs in month m
        using the recurrence relation defined for the problem.
        """
        litter_list = [1, 1]

        for i in range(3, self.m + 1):
            litters_this_month = litter_list[i - 2] + self.k * litter_list[i - 3]
            litter_list.append(litters_this_month)

        print("\nLitter on", self.m, "month is:")

        if self.m == 1 or self.m == 2:
            return 1
        else:
            return litter_list[-1]


# Example usage
R = Rabbit_recurrence(5, 3)
print(R.Rabbit_rec())
