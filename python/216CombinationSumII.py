class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []
        
        current = []
        
        
        def backtrack( n , current , i  ):
            
            if n < 0 :
                return

            if n == 0 and len(current) == k:
                res.append(current.copy())
                return

            for j in range( i, 10 ):
                
                current.append(j)
                
                backtrack(n - j, current, j+1)
                
                current.pop()
            
            return

        backtrack(n, current, 1)
        
        return res