class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        s = 0
        
        d = deque()
        
        
        #print(nums)
        
        for i,n in enumerate(nums):

            '''
            while d and d[0][1] - i > k:
                d.popleft()

            nums[i] += d[0][0] if d else 0

            while d and d[-1][0] < nums[i]:
                d.pop()
            
            if nums[i] > 0:
                d.append([nums[i],i])
            '''
            
            while d and abs(d[0][1] - i) > k:
                d.popleft()
            
            
            if d:
                nums[i] += d[0][0] 
            
            while d and d[-1][0] < nums[i]:
                d.pop()
            
            if nums[i] >= 0:
                d.append([nums[i],i])
            
            #print(d)

        #print(nums)
        return max(nums)