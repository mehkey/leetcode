class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        tot = 0
        
        for _ in range(k):
            
            m = max(nums)
            
            nums.remove(m)
            
            tot += m
            
            nums.append(m+1)
        
        #print(nums)
        return tot