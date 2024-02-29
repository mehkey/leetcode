class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @cache
        def dp(i):
            if i == len(nums):
                return 0
            
            res = 0
            for j in range(i+1,len(nums)):
                res = max( res, dp(j) + 1 if nums[j] > nums[i] else 0)
            return res

        m = 0
        for i in range(len(nums)):
            m=max(m,dp(i))
        return m + 1
        
        LIS = len(nums) * [1]
        #print(LIS)
        for i in range(len(nums)-2,-1,-1):
            
            curLongest = 1

            for j in range(i+1,len(nums)):

                if(nums[i] < nums[j]):
                    curLongest = max(1+LIS[j],curLongest )
               
            LIS[i] = curLongest
            
            #print("LIS[i]",LIS[i])
        return max(LIS)
        '''
        s = []

        for n in nums:
            while s and s[-1] >= n:
                s.pop()
            
            s.append(n)

        return len(s)

        
        @lru_cache(10_000)
        def dp(i, m):
            if i == len(nums):
                return 0

            if nums[i] > m:

                return max( dp(i+1,nums[i]) + 1 , dp(i+1,m) )

            return dp(i+1,m)

        #for i, n in enumerate( nums ):
        #    res = max( res, dp(i,n) + 1)

        return dp(0,-10**4) 
        '''