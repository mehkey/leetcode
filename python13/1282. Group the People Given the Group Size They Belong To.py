class Solution:
    def groupThePeople(self, gs: List[int]) -> List[List[int]]:
        d = defaultdict(lambda : [] )

        for i,s in enumerate(gs):
            
            d[s].append(i)
        
        res = []
        for k,v in d.items():
            cur = []
            while v:
                for _ in range(k):
                    cur.append(v.pop())
                res.append(cur)
                cur = []
        
        return res