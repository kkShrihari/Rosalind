class K_mers:
    """
    A class to compute unique and overlapping k-mers in a sequence.
    """

    def number_of_unique_kmers(self, s, k):
        """
        Extracts all unique non-overlapping k-mers from a sequence.
        """
        x = len(s)
        y = x / k
        
        i = 0
        A = 0
        B = k
        list0 = []
        result1 = []
        while i < y + k:
            for z in s:
                list1 = list(s[A:B])
                A += k
                B += k
                if list1 != list0:
                    if len(list1) == k:
                       result = ["".join(map(str, list1))]
                       result1.extend(result)
                       i += 3
        return result1
      
    def list_kmers(self, s, k):
        """
        Extracts all overlapping k-mers from a sequence.
        """
        x = len(s)
        y = x / k
        
        i = 0
        A = 0
        B = k
        list0 = []
        final_list = []
        while i < k:
            for z in s:
                list1 = list(s[A:B])
                A += 1
                B += 1
                if list1 != list0:
                    if len(list1) == k:
                        result = ["".join(map(str, list1))]
                        final_list.extend(result)
                        i += 1
        return final_list
