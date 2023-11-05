class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        
        '''
        
        '''
        n = len(nums)
        m = float('inf')
        for i in range(1,n-1):
            
            for j in range(0,i):
                
                if nums[j] >= nums[i]:
                    continue

            
                for k in range(i,n):
                    
                    if nums[k] >= nums[i]:
                        continue
                    t = nums[k] + nums[i] + nums[j]
                    
                    m = min(m,t)
        
        return m if m!= float('inf') else -1