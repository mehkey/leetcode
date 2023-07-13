class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        #for i in range(nums):

        s = sum(nums)
        n = len(nums)

        return n*(n+1)//2 - s