class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        
        def validRow( board: List[List[str]],row:int)-> bool:
            m = {}
            for i in range(0,9):
                
                n = board[i][row] 

                if not n == "." and m.get(n):
                    return False
                m[n] = n
            return True
        
        def validColumn( board: List[List[str]],column:int)-> bool:
            m = {}
            for i in range(0,9):
                
                n = board[column][i] 
                if not n == "." and m.get(n):
                    return False

                m[n] = n
            return True
        
        def validSquare( board: List[List[str]],x:int,y:int)-> bool:
            m = {}
            for i in range(0,3):
                for j in range(0,3):
                    n = board[3*x+i][3*y+j] 
                    if not n == "." and m.get(n):
                        return False
                    m[n] = n
            return True
            
        for i in range(0,9):
            if not validColumn(board,i):
                return False
        
        for i in range(0,9):
            if not validRow(board,i):
                return False
        
        
        for i in range(0,3):
            for j in range(0,3):
                if not validSquare(board,i,j):
                    return False

        return True