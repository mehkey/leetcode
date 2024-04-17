class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        N = len(nums)
        for i in range(N):
            for j in range(i+1,N):
                if (nums[i] | nums[j]) & 1  == 0 :
                    return True
        
        return False