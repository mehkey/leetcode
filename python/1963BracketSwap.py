class Solution:
    def minSwaps(self, s: str) -> int:
        
        
        closeCount = 0
        maxClose = 0
        
        for c in s:
            if c == ']':
                closeCount += 1
            else:
                closeCount -= 1
            
            maxClose = max(maxClose, closeCount)
            
        return (maxClose + 1) // 2
            