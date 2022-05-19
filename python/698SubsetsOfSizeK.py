class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums) % k :
            return False
        
        used = [ False] *  len(nums)
        #nums.sort(reverse=True)
        target = sum(nums) / k
        
        
        def backtrack( i , k , currentSum):
            
            if k == 0:
                return True
            
            if target == currentSum :
                return backtrack( 0, k -1 , 0)
        
            
            for j in range(i , len(nums)):
                if used[j] or  currentSum + nums[j] > target:
                    continue

                used[j] = True

                if backtrack( j + 1 , k , currentSum + nums[j] ):
                    return True

                used[j] = False

            return False
        
        return backtrack( 0 , k, 0)