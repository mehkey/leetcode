class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        res = []


        c = Counter(nums)

        while c:
            cur = []
            for k,v in c.items():
                cur.append(k)
                c[k]-=1
            for k in list(c.keys()):
                 if c[k] == 0:
                    del c[k]
            
            res.append(cur)

        return res