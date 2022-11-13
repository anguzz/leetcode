'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation
'''

class Solution:
    #using Stack
    def rotate(self, matrix: List[List[int]]) -> None:
        s = [val for row in matrix for val in row] # init stack
        for y in range(len(matrix)):              # traverse matrix columns
            for x in range(len(matrix)-1, -1, -1): # traverse matrix rows in reverse
                matrix[x][y] = s.pop() # modify matrix by popping from stack
        
    #transposing matrix 
    def rotate(self, matrix: List[List[int]]) -> None:
        # first we transpose the matrix.
        for x in range(len(matrix)):
            for y in range(x):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]       
		# reverse matrix after
        for x in matrix:
            x.reverse()
                
                

            
        
