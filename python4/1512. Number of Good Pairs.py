class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        
        return sum(map(lambda x:x*(x-1)//2,c.values())) 