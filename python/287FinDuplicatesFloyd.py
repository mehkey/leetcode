class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #hashset = set()

        count = 0
        for n in nums:
            count = count ^ n

        for i in range(1, len(nums)):
            count = count ^ i

        return count
