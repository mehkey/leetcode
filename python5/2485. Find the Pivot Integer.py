class Solution:
    def pivotInteger(self, n: int) -> int:
        
        total = n * (n + 1) // 2
        
        count = 0
        
        for i in range(1,n+1):
            
            count += i
            
            if count == total:
                return i
            
            total -= i
            
        return -1