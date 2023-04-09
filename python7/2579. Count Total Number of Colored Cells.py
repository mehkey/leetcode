class Solution:
    def coloredCells(self, n: int) -> int:
        
        #1   1 + 0
        #2 5 1 + 4
        #3 13 5 + 8
        #4 25 13 + 12
        
        
        prev = 1

        result = 0
        
        for i in range(n):
            
            result = prev + 4*i
            
            prev = result
        
        return result
