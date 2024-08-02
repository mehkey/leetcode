class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        #c = Counter(nums)
        '''
        c = Counter(nums)
        
        l = len(nums) // 2
        
        for k,v in c.items():
            if v > 2:
                return False
        
        return True
    
        '''
        return all([v <= 2 for v in Counter(nums).values()])