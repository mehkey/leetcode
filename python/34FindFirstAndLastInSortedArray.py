class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l = bisect.bisect_left(nums,target)
        r = bisect.bisect_right(nums,target)

        return [l , r -1] if r > 0 and l < len(nums) and nums[l] == target and nums[r-1]== target else [-1,-1]

        """
        def search(n):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) / 2
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        lo = search(target)
        return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]
        """