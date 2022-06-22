class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["." for i1 in range(n)] for i2 in range(n)]
            
        #row = set()
        col = set()
        posd = set()
        negd = set()
            
        res = 0
        
        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return
            
            for c in range(n):
                
                if c in col or (r+c) in posd or (r-c) in negd:
                    continue
                
                col.add(c)
                posd.add(r+c)
                negd.add(r-c)
                board[r][c] = 'Q'
                backtrack(r+1)

                col.remove(c)
                posd.remove(r+c)
                negd.remove(r-c)
                board[r][c] = '.'
    
        backtrack(0)
        
        return res