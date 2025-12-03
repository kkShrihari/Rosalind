class Mortal_Fibonacci_sequence:
    """
    A class that computes the total number of rabbit pairs after a given
    number of months, assuming rabbits die after a fixed lifespan.
    """
    def __init__(self, x, y):
        """
        Initializes the simulation.

        Parameters:
        x (int): Total number of months to simulate.
        y (int): Rabbit lifespan in months.
        """
        self.month = x
        self.death = y
    
    def MFS(self):
        """
        Computes the mortal Fibonacci sequence by tracking rabbit age cohorts
        and summing the total number alive in the final month.
        """
        MFS_month  = [0] * self.death
        MFS_month[0] = 1   # start with newborns at age 0
        
        if self.month == 1 or self.month == 2:
            return 1
        
        for i in range(2, self.month + 1):
            copy_MFS = MFS_month.copy()
            print(copy_MFS, "hi", i-1)
            MFS_month = [0] * self.death

            for m in range(len(copy_MFS)):
                if copy_MFS[m] != 0:
                    if (m != (len(copy_MFS)-1)) and (m == 0):
                        MFS_month[1] += copy_MFS[0]

                    if (m != (len(copy_MFS)-1)) and (m == 1):
                        MFS_month[m+1] += copy_MFS[1]
                        MFS_month[0]   += copy_MFS[m]

                    if (m > 1) and (m != (len(copy_MFS)-1)):
                        MFS_month[m+1] += copy_MFS[m]
                        MFS_month[0]   += copy_MFS[m]

                    if m == (len(copy_MFS)-1):
                        MFS_month[0]   += copy_MFS[m]

            total = 0
            for no in MFS_month:
                total = total + no  

        return total

# Example
MFS1 = Mortal_Fibonacci_sequence(6,3) 
print(MFS1.MFS()) 
