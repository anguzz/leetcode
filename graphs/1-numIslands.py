#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        xlen = len(grid)
        ylen = len(grid[0])
        visited = set() 
        d = [(1,0),(0,1),(-1,0),(0,-1)]
        ans = 0
        
        
        
        def dfs(x, y):
	## adding the row and column number to the visited set
            visited.add((x,y))
            for dx, dy in d:  
                xpos = x + dx  #update x and y
                ypos = y + dy
			
                if( xpos < 0 or xpos >= xlen or 
                    ypos < 0 or ypos >= ylen or
                    grid[xpos][ypos] == '0' or
                    (xpos, ypos) in visited):
                    continue
	## if all the conditions are met, function is called recursively
                dfs(xpos, ypos)
                
        for x in range(xlen):
            for y in range(ylen):
                if grid[x][y] == '1' and (x,y) not in visited:
                    dfs(x, y)
		## when dfs completes, island has been found
		## so increase the answer
                    ans += 1
        return ans
