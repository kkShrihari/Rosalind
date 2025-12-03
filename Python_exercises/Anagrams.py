def anagrams(words):
    """
    Groups words into anagram sets by sorting letters.
    Returns the largest set of anagrams as a Python set.

    Parameters:
        words (list): List of strings.

    Returns:
        set: Largest set of anagrams found.
    """
    dict1 = {}
    for x in words:
        word1 = ''.join(sorted(x))
        if word1 in dict1:
            dict1[word1].append(x)
        else:
            dict1[word1] = [x]
    Anagram = max(dict1.values(), key=len)
    return set(Anagram)
