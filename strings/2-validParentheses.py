class Solution:
    def isValid(self, s):
        stack = []
        for i in s:   #go through string
            if i in '({[':   #if we have opening bracket
                stack.append( ')}]'  [ '({['.index(i)]  ) #append closing bracket to the index the opening bracket is at in the string
            elif stack and stack[-1] == i:   
                stack.pop()
            else:
                return False
        return len(stack) == 0
