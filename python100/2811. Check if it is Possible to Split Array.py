class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        @cache
        def dp(i,j):
            
            #print(i,j)
            if i == j:
                return True

            if i == j -1:
                return True
            

            '''
            if s >= m : 
                return dp(i+1)

            for j in range(i+1,len(nums)):

                s += nums[j]

                if s >= m and dp(j+1):
                    return True

            return False
            '''

            if sum(nums[i+1:j+1]) >= m:
                if dp(i+1,j):
                    return True
            
            if sum(nums[i:j]) >= m:
                if dp(i,j-1):
                    return True
            
            return False
            
        return dp(0,len(nums)-1)

