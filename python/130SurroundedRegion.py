class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board) #3
        n = len(board[0]) #3
        
        dirs = [[0,-1],[-1,0],[1,0],[0,1]]
        
        def bfs(i,j):

            
            if  (i <= 0 or j <= 0 or i >= (m -1) or j >= (n -1)  ):
                return
            
            if (board[i][j] == 'X'):
                return
            if (board[i][j] == 'T'):
                return
                
            board[i][j] = 'T'
            
            
            for d in dirs:
                    bfs(i+d[0],j+d[1])

        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == (m -1) or j ==( n -1)) and board[i][j]=='O':

                    board[i][j] = 'T'

                    for d in dirs:
                        bfs(i+d[0],j+d[1]) 
        #print(board)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j] = 'X'
        #print(board)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='T':
                    board[i][j] = 'O'
        
        return board
        
        