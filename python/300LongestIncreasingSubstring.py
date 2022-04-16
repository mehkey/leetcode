class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        LIS = len(nums) * [1]
        #print(LIS)
        for i in range(len(nums)-2,-1,-1):
            
            curLongest = 1

            for j in range(i+1,len(nums)):

                if(nums[i] < nums[j]):
                    curLongest = max(1+LIS[j],curLongest )
               
            LIS[i] = curLongest
        
        
        return max(LIS)