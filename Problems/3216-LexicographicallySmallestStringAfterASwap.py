# url: https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

class Solution:
    def getSmallestString(self, s: str) -> str:
        charList = list(s)
        for i in range(len(charList) - 1):
            print(int(charList[i]) % 2)
            if int(charList[i]) % 2 == int(charList[i + 1]) % 2 and int(charList[i]) > int(charList[i + 1]):
                charList[i], charList[i + 1] = charList[i + 1], charList[i]
                newString = ''.join(charList)
                return newString
        
        return s

