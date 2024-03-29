class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        m = len(nums)//2
        i, j = 0, m
        res = 0
        nums.sort()
        while i < m and j < len(nums):
            if nums[j] >= nums[i]*2:
                res += 2
                i += 1
            j += 1
        return res