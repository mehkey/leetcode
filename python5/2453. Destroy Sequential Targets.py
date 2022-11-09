class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        
        
        #1,3,5,7,9,... 
        
        #3, 5, 7, 9
        
        #8, 10, 
        
        #nums = [3,7,8,1,1,5], space = 2
        
        groups = defaultdict(int)
        val = defaultdict(list)

        for n in nums:
            groups[n%space] += 1
            val[n%space].append(n)

        n = max(groups.values())
        m = float('inf')
        
        for v in val:
            if len(val[v]) == n:
                m = min(m, min(val[v]))
        
        return m
        
        