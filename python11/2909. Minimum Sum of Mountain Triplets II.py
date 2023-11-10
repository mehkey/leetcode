class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        m = float('inf')
        
        #[8,6,1,5,3]
        #[8,6,1,5,3]
        #[8,6,1,1,1]
        #[1 1 1 3 3]
        
        left = [float('inf')]* n
        right = [nums[-1]]*n
        
        for i in range(n):
            left[i] = min(nums[i], left[i-1])
        
        for i in range(n-2,-1,-1):
            right[i] = min(nums[i], right[i+1])
        
        print(left,right)
        
        
        for i in range(1,n-1):
            if right[i+1] >= nums[i] or left[i-1] >= nums[i]:
                continue

            m = min(m, nums[i] + left[i-1] + right[i+1] )

        return m if m!= float('inf') else -1

        '''
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
        '''