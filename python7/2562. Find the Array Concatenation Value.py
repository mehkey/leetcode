class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
        c = 0
        
        
        while nums:
            l = str(nums[0])
            
            
            nums = nums[1:]
            if nums:
                r  = str(nums[-1])
                nums = nums[:-1]
                
                c += int(l+r)

            else:
                c += int(l)
            
            #print(c)
        return c