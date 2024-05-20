# url: https://leetcode.com/problems/top-k-frequent-elements/

# -------------------------------------------------------------------- #

from typing import List

class Solution:

    '''
    This solution uses a dictionary to count the frequency of each element in the input list. We then create a list of lists, where each list at index i contains the elements that appear i times in the input list. We iterate through this list of lists in reverse order, adding the elements to the result list until we have k elements. We return the result list when we have k elements.
    '''

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

'''

----------
This version has comments for illustrating what's happening at each step of the way.
----------

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
            print("Added ", n, "to dictionary")
            print(count)
        print()
        
        for n, c in count.items():
            print("key:", n, "has", c, "occurences. Input into freq array.")
            freq[c].append(n)
            print("Result array:", freq)
        print()
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                print("Take values from high end of freq array until have length of k: ")
                res.append(n)
                print(res)
                if len(res) == k:
                    return res

'''