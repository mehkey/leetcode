class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)
        c = Counter()

        for n in nums:
            c[n]+= 1
            if c[n] == ceil(N/2):
                return n

        return -1
