class Solution:
    def countTestedDevices(self, bp: List[int]) -> int:
        n = len(bp)
        res = 0
        for i,b in enumerate(bp):
            if b > 0:
                res += 1
                for j in range(i+1,n):
                    bp[j]-=1
        
        return res