class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] :
                continue
            
            l = i+1
            r = len(nums) -1
            while(l<r):
                treeSum = nums[i] + nums[l] +nums[r]
                
                if treeSum > 0 :
                    r = r-1
                elif treeSum < 0 :
                    l = l+1
                else :
                    res.append([nums[i],nums[l],nums[r]])
                    l = l +1
                    while l < r and nums[l] == nums[l-1]:
                        l = l+1
        return res