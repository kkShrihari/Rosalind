import math 

class Model_random_genome:
    """
    A class to compute the log10 probability of observing a DNA string
    under different GC-content values using a random genome model.
    """

    def __init__(self, str_input, array):
        """
        Parameters:
        str_input (str): DNA sequence consisting of A, T, G, C.
        array (str): Space-separated list of GC-content probabilities (floats).
        """
        self.str_input = str_input
        self.array = array
    
    def MRG(self):
        """
        Calculates log10 probabilities for the DNA sequence under each provided
        GC-content value, assuming:
        - G and C share GC proportion equally (x/2 each)
        - A and T share AT proportion equally ((1-x)/2 each)

        Returns:
        str: Space-separated list of log10 probabilities rounded to 3 decimals.
        """
        vec1 = [float(x) for x in self.array.split(" ")]
              
        g = self.str_input.count("G") + self.str_input.count("C")
        a = self.str_input.count("A") + self.str_input.count("T")

        sum = ""
        for no in range(len(vec1)):
            x = float(vec1[no])
            if x <= 0 or x >= 1:
                raise ValueError(f"x must be between 0 and 1 (exclusive), got {x}")
    
            val1 = g * math.log10(x / 2)
            val2 = a * math.log10((1 - x) / 2)
            temp = val1 + val2
            sum += str(float(round(temp,3))) + " "

        print("\n")
        return sum
