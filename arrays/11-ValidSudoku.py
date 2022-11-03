#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules: Cells with . are empty.
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols= collections.defaultdict(set)
        rows= collections.defaultdict(set) 
        sqrs= collections.defaultdict(set) 
        
        
        for x in range(9):
            for y in range(9):
                if board[x][y]==".": 
                    continue
                if (board[x][y] in cols[x] or  
                    board[x][y] in rows[y] or
                    board[x][y] in sqrs[(x//3, y//3)]):
                    return False
                else:                            
                    cols[x].add(board[x][y])
                    rows[y].add(board[x][y])
                    sqrs[(x//3, y//3)].add(board[x][y]) 
        return True
        
         '''
        check row for dupes function
        check column for dupes function  
        check 3*3 subbox for dupes, to do this find any x,y coord and divide by 3
        if any dupes found==false, otherwise add to seen set
        do this using hash  
        '''
