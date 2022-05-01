class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        if len(word) ==0:
            return False
        
        if len(board) == 0 or len(board[0]) == 0:
           return False
    
        directions = [[0,-1],[1,0],[0,1],[-1,0]]

        path = set()
        
        def dfs(x,y, i ):
        
            if i  == len(word) :
                return True
            
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or (x,y) in path or board[x][y] != word[i]:
                return False
            
            
            
            path.add((x,y))
            for direction in directions :
                
                if dfs(x+direction[0],y+direction[1],i+1 ) :
                    return True

            path.remove((x,y))
            return False
        

        first = word[0]
        
        for x in range(0, len(board)):
            for y in range(0, len(board[0])):
                
                if(board[x][y] == first):
                    if dfs(x,y, 0 ) :
                        return True
        
        return False
        
        
        
                                
                
                       
                    
                    