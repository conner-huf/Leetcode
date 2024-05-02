from typing import List

class Solution:

# --------------------------------------------------------------------#

    '''
    The brute force solution is to just iterate through each value in the array, searching each other value for a matching value. If we find a match, we return True, otherwise, return False. 
    
    Time Complexity: O(n^2)
    Space Complexity: 0(1)
    '''

    def containsDuplicate_BruteForce(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False

# --------------------------------------------------------------------#

    '''
    This solution uses the fact that the array is an array of numbers. We can sort the array, then any duplicates will be adjacent to one another. This allows us to iterate through the sorted array once and check if the current value is equal to the next value. This is an improvement over the brute force solution, but we have to sort the array. This sorting step causes the solution to have a time complexity of O(nlogn) instead of O(n).
    
    Time Complexity: 0(nlogn)
    Space Complexity: 0(1)
    '''
    def containsDuplicate_Sort(self, nums: List[int]) -> bool:
        sortedNums = sorted(nums)
        for i in sortedNums:
            if sortedNums[i] == sortedNums[i+1]:
                return True
        
        return False
    
# --------------------------------------------------------------------#

    '''
    This solution uses a set to store unique values. This way, we can iterate through the array of nums only one time, checking if the value is in the set. If it is, we return True, otherwise, add the value into the set and continue iterating through the array. Once we reach the end without returning, we know there are no duplicates and return false. We have a tradeoff of using a bit more memory to store the set, but this allows us to get a time complexity of O(n).

    Time Complexity: O(n)
    Space Complexity: O(n)
    '''

    def containsDuplicate_Set(self, nums: List[int]) -> bool:
        set = set()
        for num in nums:

            if num in set:
                return True
            else:
                set.add(num)
        
        return False
