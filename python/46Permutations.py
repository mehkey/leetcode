class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        if(len(nums) == 1):
            return [nums.copy()]
        
        for i in range(len(nums)):
            val = nums.pop(0)
            
            temp = self.permute(nums)
            
            for j in temp:
                j.append(val)
            
            res.extend(temp)
            
            nums.append(val)
        
        return res