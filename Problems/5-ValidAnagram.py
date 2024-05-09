
# URL: https://leetcode.com/problems/valid-anagram/
# -------------------------------------------------------------------- #

class Solution:

# -------------------------------------------------------------------- #

    '''
    This solution uses the built-in Python function sorted() to sort the strings. If the sorted strings are equal, we return True, otherwise, we return False.

    Time Complexity: O(nlogn)
    Space Complexity: O(1)
    '''

    def isAnagram_Sort(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        '''
        adding an early return here for this case can improve performance. In the case that the lengths of the strings are different, we know they can't be anagrams, so why bother using nlogn time to sort them?
        '''
        return sorted(s) == sorted(t)

# -------------------------------------------------------------------- #

    '''
    This solution iterates through the first string, adding each character to a dictionary. If the letter exists already in the dictionary, the value of it's key is incremented by 1. Then, we iterate through the second string, decrementing the value of the keys in the dictionary. If we find a key that doesn't exist in the dictionary, or if the value of the key is less than 0, we return False. If we reach the end of the second string without returning, we return True.

    Time Complexity: O(n)
    Space Complexity: O(n)
    '''

    def isAnagram_Dict(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        charDict = {}

        for char in s:
            charDict[char] = charDict.get(char, 0) + 1

        for char in t:
            charDict[char] = charDict.get(char, 0) - 1
            if charDict[char] < 0:
                return False

        return True

# -------------------------------------------------------------------- #
