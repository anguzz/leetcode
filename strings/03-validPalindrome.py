class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = re.sub(r'[^0-9a-z]', '', s.lower()) #cleaned string
        return all(s2[i]==s2[~i] for i in range(int(len(s2)/2)))
         
           
'''
then compare using all function checking i with the complement of i, 
all checks every item in list are true returns true if so, if not false

how invert operator works in this case
i  ~i
-----
0  -1
1  -2
2  -3
3  -4 
4  -5 
5  -6
'''
