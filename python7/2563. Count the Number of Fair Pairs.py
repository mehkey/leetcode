class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # First, note that the answer does not change if we sort the array
        nums.sort()
        fairCtr = 0
        for i in range(len(nums)):
            # For each index find the left and right elements for which the sums lie between lower and upper
            l = bisect_left(nums, lower - nums[i])
            r = bisect_right(nums, upper - nums[i])
            fairCtr += (r - l)
            # check if index i lies in the interval, subtract one (we don't want to double count index i)
            if l <= i < r:
                fairCtr -= 1
        return fairCtr // 2

    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:

        f = lambda x: sum(bisect_right(nums, x - num, hi=i)
                       for i, num in enumerate(nums))
        nums.sort()

        return f(upper) - f(lower - 1)
    

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans=0
        for i in range(len(nums)-1, -1, -1):
            v = nums[i]
            a = bisect_left(nums, lower - v, lo=0, hi=i)
            b = bisect_right(nums, upper - v, lo=0, hi=i)
            ans += b - a
        return ans 