class Permutations:
    """
    A class to compute partial permutations P(n, k) = n! / (n-k)!
    and return the result modulo 1,000,000.
    """
    def __init__(self, n, k):
        """
        Initializes the permutation calculator.

        Parameters:
        n (int): The upper bound (1 ≤ n ≤ 100)
        k (int): Number of items selected (1 ≤ k ≤ 10, k ≤ n)
        """
        self.n = n
        self.k = k

    def Perm_calc(self):
        """
        Computes the number of partial permutations P(n, k),
        applies modulo 1,000,000, and returns the integer result.

        Returns:
        int: P(n, k) mod 1,000,000
        """
        print("\n")
        if not (1 <= self.n <= 100):
            raise ValueError("n must be between 1 and 100")
        if not (1 <= self.k <= 10):
            raise ValueError("k must be between 1 and 10")
        if (self.k > self.n):
            raise ValueError("K cant be bigger than n")

        result = 1
        for i in range(1, self.n + 1):
            result = result * i

        result1 = 1
        sub = self.n - self.k
        for i in range(1, sub + 1):
            result1 = result1 * i

        partial_perm = result / result1

        '''Modulo of billion' = 1,000,000'''
        M_of_perm = partial_perm % 1000000
        return(int(M_of_perm))


P1 = Permutations(21, 7)
print(P1.Perm_calc())
