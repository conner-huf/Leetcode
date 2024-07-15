# url: https://leetcode.com/problems/min-stack/

# -------------------------------------------------------------------- #

'''
This solution uses two stacks to keep track of the values and the minimum values. When a new value is pushed onto the stack, we check if it is less than the current minimum value. If it is, we push the new value onto the minStack. Otherwise, we push the current minimum value onto the minStack. When a value is popped from the stack, we also pop the top value from the minStack. The top value of the minStack is always the minimum value in the stack.
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()