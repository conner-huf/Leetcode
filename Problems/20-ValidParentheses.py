
# url: https://leetcode.com/problems/valid-parentheses/
# -------------------------------------------------------------------- #

class Solution:

# -------------------------------------------------------------------- #
    
    '''
    This solution uses a stack to keep track of the opening parentheses. We iterate through the string and push the opening parentheses onto the stack. When we encounter a closing parenthesis, we check if the stack is empty or if the last element in the stack is the corresponding opening parenthesis. If it is, we pop the opening parenthesis from the stack. If the stack is empty at the end of the iteration, we return True, otherwise we return False.

    We use a dictionary to map the closing parentheses to their corresponding opening parentheses. This allows us to easily check if the last element in the stack is the corresponding opening parenthesis. If it is not, we return False.

    Time complexity: O(n)
    Space complexity: O(n)
    '''

    def isValid(self, s: str) -> bool:
            stack = []
            closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
            
            for c in s:
                if c in closeToOpen:
                    if stack and stack[-1] == closeToOpen[c]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(c)
            
            if not stack:
                return True
            
            return False
            