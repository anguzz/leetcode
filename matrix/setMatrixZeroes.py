class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        col = []
        row = []
        for i in range(len(matrix)):            #iterate and record zeros in rows/cols
            for j in range(len(matrix[0])):   
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
                    
        for i in col:                         #set zeroes in the recorded pos
            for j in range(len(matrix)):
                matrix[j][i] = 0   
        for i in row:               
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
