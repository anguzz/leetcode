class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        xd=len(matrix) #x distance
        yd=len(matrix[0]) #y distance
        
        x = []
        y = []
        
        for i in range(len(matrix)):      #iterate & record zeros in rows/cols
            for j in range(len(matrix[0])):   
                if matrix[i][j] == 0:
                    x.append(i)
                    y.append(j)
                    
        for i in x:               #overwrite any x matrix position based on our recorded x pos 
            for j in range(xd): 
                matrix[j][i] = 0   
        for i in y:               #do the same for any y positions         
            for j in range(yd):  
                matrix[i][j] = 0
