class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        prev= 0
        res = []
        for n in nums:
            res.append(prev+n)
            prev = prev+n
        return res

        return list(accumulate(nums))