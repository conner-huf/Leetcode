from collections import defaultdict
from typing import List

# url: https://leetcode.com/problems/group-anagrams/

# -------------------------------------------------------------------- #

'''
This solution uses a dictionary to map the character count of each string to a list of anagrams. We use a default dict because it defaults to an empty list if the key does not exist, which we can then append to. We iterate through the list of strings and for each string, create a list of 26 elements, one for each letter of the alphabet. We iterate through the string and increment the count of each letter in the list. We then convert the list to a tuple and use that as the key in the dictionary. We append the string to the list of anagrams for that key. At the end, we return the values of the dictionary.

Time complexity: O(n * m) where n is the number of strings and m is the length of the longest string
Space complexity: O(n)
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 
        # default value of a key is an empty list

        for s in strs:
            count = [0] * 26
            # an array of 26 0s, representing each letter of alphabet

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            '''
            if we have the character "a", and we want to map that to index 0, we can do that by subtracting the result of it's ord() by ord('a'). Since ASCII is ordered, we can subtract any character's ord() by ord('a') to get the index of that character in the list.

            python doesn't allow for lists to be keys in a dictionary. Cast the list to a tuple to use as a key
            '''

            res[tuple(count)].append(s)

        return res.values()
    