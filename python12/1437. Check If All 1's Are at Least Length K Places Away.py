class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        last = -1
        for i in range(n):
            if nums[i] == 1:
                if last == -1:
                    last = i
                elif i - last <= k:
                    return False
                else:
                    last = i
        
        return True