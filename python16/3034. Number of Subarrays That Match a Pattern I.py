class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        
        N = len(nums)
        M = len(pattern)
        ans = 0
        for i in range(N-M):
            
            good = True
            for j in range(M):
                if pattern[j] == 0:
                    if not nums[i+j] == nums[i+j+1]:
                        good = False
                        break
                
                if pattern[j] == 1:
                    if not nums[i+j] < nums[i+j+1]:
                        good = False
                        break
                
                if pattern[j] == -1:
                    if not nums[i+j] > nums[i+j+1]:
                        good = False
                        break
                
            if good:

                ans += 1
        
        return ans