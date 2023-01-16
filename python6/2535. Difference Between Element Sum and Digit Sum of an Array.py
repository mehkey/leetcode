class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        s = sum(nums)
        
        arr = []
        for n in nums:
            
            arr.extend([int(i) for i in str(n)])
        
        return abs(s-sum(arr))
