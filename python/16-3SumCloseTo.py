class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        
        closest = float("inf")
        offby = float("inf")

        nums.sort()
        
        #print(nums)
        
        for i in range(0,len(nums)-2):
            
            l = i + 1
            
            r = len(nums) -1

            while l < r  :
                
                #print(i)
                #print(l)
                #print(r)

                s = nums[i] + nums[l] + nums[r]
                
                #print(s)
                #print(i, l, r)
                #print(nums[i] , nums[l] , nums[r])
                if abs(s-target) < offby :
                    offby = abs(s-target) 
                    closest = s
                
                if target == s:
                    
                    return 0
                
                if s < target:
                    l = l + 1
                elif s > target:
                    r = r - 1

        return closest
                
                
                
            
        