#Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
#For example, "ace" is a subsequence of "abcde" with length 3

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        xlen = len(text1)
        ylen = len(text2)
        m = [[0] * (ylen  + 1) for x in range(xlen + 1)]  #initalize matrix 
        
        for x in range(xlen - 1, -1, -1):
            for y in range(ylen - 1, -1, -1):  
                 
                if text1[x] == text2[y]:     #if equal add 1 and diagnol 
                    m[x][y] = 1 + m[x + 1][y + 1]
                    
                else:                       #otherwise take max of numbers under and right and update it
                    m[x][y] = max(m[x + 1][y], m[x][y + 1])
        return m[0][0]

 #the approach is to use a dp table that we buildup from a bottom up approach using a set of conditions, until we are at the end [0][0]
