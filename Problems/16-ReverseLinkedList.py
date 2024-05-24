# url: https://leetcode.com/problems/reverse-linked-list/

# ---------------------------------------------------- #

'''
    This solution uses two pointers to reverse the linked list. 

    Time Complexity: 0(n)
    Space Complexity: 0(1)
'''

# Solution 1: Iterative
class Solution:
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
# ---------------------------------------------------- #

# Solution 2: Recursive
class Solution:
    def reverseList(self, head):
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead