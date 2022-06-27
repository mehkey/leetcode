class Solution:
    def jump(self, nums: List[int]) -> int:
        
        """
        dp = [0] * len(nums)
        
        dp[len(nums)-1] = 0

        for i in range(len(nums)-2, -1, -1):
            #print(i)
            minimum = float("inf")
            
            for j in range(i+1, min(i+nums[i]+1,len(nums))):
            #last = i + nums[i]
                #if j + nums[j]:
                #print(j)
                minimum = min(minimum, 1 + dp[j])    
            
            
            dp[i] = minimum
        
        #print(dp)
        return dp[0]
        
        """
        
        l =0
        r =0
        count = 0
        
        while r < len(nums)-1:
            
            farthest = 0
            
            for i in range(l,r+1):
                farthest = max(farthest, i + nums[i])
            
            l = r+1
            r = farthest
            count += 1
            
        return count
        