class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        
        '''
        res = []
        if k >=2:
            first = [False] * len(nums)

            first[k] = True

            first[len(nums)-k-1] = True

            for i in range(k-1,-1,-1):
                first[i] = nums[i] >= nums[i+1] and first[i+1]


            for i in range(k+1,len(nums)):
                first[i] = nums[i] >= nums[i-1] and first[i-1]
        else:
            first = [True] * len(nums)

        
        for i in range(k, len(nums)-k):
            
            if first[i-k] and first[i+k]:
                res.append(i)
            
        return res
        '''
        
        n, ans= len(nums) ,[]
        dp1 , dp2= [1]*(n+1), [1]*(n+1)
        for i in range(1,n):
            if nums[i-1]>=nums[i]:  dp1[i]= dp1[i-1]+1
        
        for i in range(n-2,-1,-1):
            if nums[i]<=nums[i+1]:  dp2[i]= dp2[i+1]+1
        
        for i in range(k,n-k):
            if dp1[i-1]>=k and dp2[i+1]>=k: ans+= [i]
        return ans