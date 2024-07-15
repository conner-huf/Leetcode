# url: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# -------------------------------------------------------------------- #

'''
    This solution uses a set to keep track of the characters in the current substring. We iterate through the string, adding characters to the set. If we encounter a character that is already in the set, we remove characters from the set until the character is no longer in the set. We keep track of the length of the substring and return the maximum length of the substring without repeating characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        maxLen = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen