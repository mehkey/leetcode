class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        hm = defaultdict(int)
        for i,j in reversed(operations):
            hm[i] = hm[j] if hm[j] > 0 else j
        
        #print(hm)
        
        for i,v in enumerate(nums):
            if v in hm:
                nums[i] = hm[v]
        
        return nums