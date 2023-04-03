class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        c = Counter(nums)
        
        res = []
        
        while c:
            row = []
            keys = list(c.keys())
            for k in keys:
                row.append(k)
                c[k] -=1
                if c[k] == 0:
                    del c[k]
            
            res.append(row)
        
        return res
        