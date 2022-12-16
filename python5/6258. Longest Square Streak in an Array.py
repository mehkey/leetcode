class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        s = set(nums)
        m = 1
        for n in nums:
            count = 1
            while True:
                n = n * n
                if n in s:
                    count+=1
                else:
                    break
            m=max(m,count)
        return -1 if m == 1 else m