class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        
        #for 
        #Counter
        #groupBy
        
        nums = list(filter(lambda x: x % 2 == 0, nums))
        
        #counts = [(x, len(list(group)))
              #for x, group in itertools.groupby(nums)  ]
        
        #counts = Counter(nums)
        
        if len(nums) == 0:
            return -1
        
        #counts = Counter(nums)
        
        cc = Counter(nums)
        
        counts = []
        
        for c in cc:
            counts.append((c,cc[c]))
        
        counts.sort(key=lambda x: (-x[1], x[0]))
        
        #print(counts)
        return counts[0][0]
    
        ctr = Counter(nums)
        return max([c for c in ctr if not c%2], key = lambda x:(ctr[x], -x), default = -1)
        