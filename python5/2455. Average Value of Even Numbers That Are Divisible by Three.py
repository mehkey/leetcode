class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res = []
        for n in nums:
            if n % 3 == 0 and n % 2 == 0:
                res.append(n)
        return floor(sum(res) / len(res)) if len(res) > 0 else 0