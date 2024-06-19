class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        p  = 1
        s = 0
        for c in str(n):
            p *= int(c)
            s += int(c)
        return p - s