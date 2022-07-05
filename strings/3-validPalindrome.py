class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = re.sub(r'[^0-9a-z]', '', s.lower()) #cleaned string
        return all(s2[i]==s2[~i] for i in range(int(len(s2)/2)))
         
           
