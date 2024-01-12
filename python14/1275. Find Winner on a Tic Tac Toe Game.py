class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        aa = []
        grid = [['']*3 for _ in range(3)]
        a = True
        for r,c in moves:
            
            if a:
                grid[r][c] = 'A'
            else:
                grid[r][c] = 'B'
            
            a = not a
        
        for i in range(3):
            if all(grid[i][j] == 'A' for j in range(3)):
                return 'A'
            if all(grid[i][j] == 'B' for j in range(3)):
                return 'B'
        
        for j in range(3):
            if all(grid[i][j] == 'A' for i in range(3)):
                return 'A'
            if all(grid[i][j] == 'B' for i in range(3)):
                return 'B'
        
        if all(grid[k][k] == 'A' for k in range(3)):
            return 'A'
        if all(grid[2-k][k] == 'B' for k in range(3)):
            return 'B'
        
        if all(grid[k][k] == 'B' for k in range(3)):
            return 'B'
        if all(grid[2-k][k] == 'A' for k in range(3)):
            return 'A'

        return 'Pending' if len(moves) != 9 else 'Draw'
