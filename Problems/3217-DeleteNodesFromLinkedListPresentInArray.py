from typing import List
from typing import Optional
from typing import ListNode

# url: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        numSet = set(nums)
        curr = dummy

        while curr.next:
            if curr.next.val in numSet:
                print(curr.next.val, "exists in nums. Moving to next node")
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next