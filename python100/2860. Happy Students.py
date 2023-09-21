class Solution:
    def countWays(self, nums: List[int]) -> int:
        
        hm = {}
        
        nums.sort()
        tt = 1
        
        #print(nums)
        
        t = 0
        
        #if nums[0] > 0:
        #    t += 1
        
        for i  in range(0,len(nums)-1):
            #print("tt",tt,"n",n)
            
            n = nums[i]
            np = nums[i+1]
            

            if tt > n or tt < np:
                t += 1

            tt += 1
        
        if tt > nums[len(nums)-1]:
            t += 1
        
        return t
        