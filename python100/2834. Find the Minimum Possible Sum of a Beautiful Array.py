class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        
        
        s= set()
        
        t = 0
        tt = 0
        for i in range(1,2*n):
            if target - i in s:
                pass
            else:
                s.add(i)
                t += i
                tt += 1
            
            if tt == n:
                return t
            
            