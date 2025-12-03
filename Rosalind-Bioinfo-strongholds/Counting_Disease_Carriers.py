class Counting_Disease_Carriers:
    """
    A class to estimate the proportion of heterozygous disease carriers
    given allele frequencies under Hardy–Weinberg equilibrium.
    """
    print("\n")

    def __init__(self, input):
        """
        Parameters:
        input (str): Space-separated list of disease prevalence values (q²).
        """
        self.input  = input
    
    def Counting_DC(self):
        """
        Computes carrier probability using:
        q = sqrt(q²)
        carriers = 2q − q²

        Returns:
        str: Space-separated carrier probabilities rounded to 3 decimals.
        """
        str_list = list(self.input.strip().split(" "))
        print_it = ""
        for i in range(len(str_list)):
            q = math.sqrt(float(str_list[i]))
            # 2pq + q² = 2q(1−q) + q² = 2q − q²
            final = 2*q - q**2
            print_it += f"{final:.3f} "
        return print_it
        


input = "0.1 0.25 0.5"
CDC = Counting_Disease_Carriers(input)
print(CDC.Counting_DC())
