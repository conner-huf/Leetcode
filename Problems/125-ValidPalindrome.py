
# url: https://leetcode.com/problems/valid-palindrome/
# -------------------------------------------------------------------- #

class Solution:

# -------------------------------------------------------------------- #

    '''
    This solution uses two pointers to iterate through the string. We use the definition of a palindrome (being a string that is the same forwards and backwards) to come up with the idea of comparing the characters at both ends and sequentially iterating toward the middle. Python has a built in function, isalnum(), that checks if a character is alphanumeric, but we can create our own function for the sake of completion and understanding the concept.

    Time complexity: O(n)
    Space complexity: O(1)
    '''

    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
        
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    
# -------------------------------------------------------------------- #
