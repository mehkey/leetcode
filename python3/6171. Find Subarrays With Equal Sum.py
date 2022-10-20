class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        
        c = Counter(nums)
        
        for i in range(len(nums)-1):
            k = i+1
            for j in range(i+1, len(nums)-1):
                l = j+1
                if (nums[i] + nums[k] == nums[j] + nums[l]):
                    return True
                
            '''for j in range(i+1, len(nums)):

                    for k in range(i+1,len(nums)):
                        
                        for l in range(j+1,len(nums)):
                            
                            if (v1 + nums[k] == nums[j] + nums[l]):
                                print(v1,nums[k], nums[j], nums[l])
                                return True
            '''
        return False
                            
                            
                            