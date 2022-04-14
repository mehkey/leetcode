class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        #current max and current min
        cache = [1,1];
        maxValue = max(nums)

        for i in range(len(nums)):
            
            if nums[i] > 0 :
                cache[0] = max( nums[i], cache[0] * nums[i])

                cache[1] = min(nums[i], cache[1] * nums[i])

                maxValue = max(maxValue, cache[0])
                
            elif nums[i] < 0 :

                curMin= cache[1]

                cache[1] = min(nums[i], cache[0]  * nums[i])
                cache[0] = max(nums[i], curMin * nums[i])
                
                maxValue = max(maxValue, cache[0])
                
            else : # == 0
                cache = [1,1]

        return maxValue;