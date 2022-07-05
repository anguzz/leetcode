class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        dict = {'(' : ')', '[' : ']', '{' : '}'}  
        stack = []                              
        for i in s:
            if i in dict.keys():
                stack.append(i)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if i!= dict[a]:
                    return False
        return stack == []
    
#first check to make sure string is even and not odd
#stack validation
#store last left bracket, use left as key and right as value
 #if store left key bracket inside stack and find right value, pop
