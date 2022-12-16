class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        s = set(nums)
        
        n = { int(str(i)[::-1]) for i in nums}
        
        s.update(n)
        
        return len(s)
        