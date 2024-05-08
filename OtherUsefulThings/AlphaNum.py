'''
Python has a built in isalnum() function that does this, but here is the logic for creating the function yourself. The function uses the ord() function to get the ASCII value of a character. Since the ASCII values of uppercase letters are sequential, as are the values for lowercase and digits, we can use these to determine if a character's ASCII value exists between those ASCII values. If it does, then it is alpha numeric.
'''

def alphaNum(self, c):
    return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))