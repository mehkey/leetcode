class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        
        mod = 10**9 + 7
        
        l = 0
        r = len(nums)-1
        
        while nums[l] != 1:
            l+=1
            if l == len(nums):
                return 0
        
        while nums[r] != 1:
            r-=1
        
        
        temp = nums[l+1:r]
        
        dp = [1] * (len(temp) +1)
        
        #print(temp)
        #print(dp)
        
        prev = 1
        count = 1
        
        total = 1
        
        for i in range(0,len(temp)):
            if temp[i] == 0:
                dp[i+1] = (prev + dp[i]) % mod
                #count += 1
                #prev = 0
            if temp[i] == 1:
                prev = dp[i]
                dp[i+1] = dp[i]
                count = 1
                #dp[i+1] = (2*(dp[i] )) % mod
        
        #print(dp)
        if not dp:
            return 1

        #print(dp)
        return dp[-1]
        
        @cache
        def dfs(i):
            if i == len(temp):
                return 1
            
            if temp[i] == 0:
                return (1+ dfs(i+1)) % mod
            
            if temp[i] == 1:
                return ((dfs(i+1) + 1)) % mod
        
        #print(temp)
        return dfs(0) % mod