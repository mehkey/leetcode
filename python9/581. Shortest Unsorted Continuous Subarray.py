class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        l = 0
        r = len(nums)-1

        ss = sorted(nums)

        for i in range(len(nums)):
            l = i
            if nums[i] != ss[i]:
                
                break

        if l == len(nums)-1:
            return 0

        for i in range(len(nums)-1,-1,-1):
            r = i
            if nums[i] != ss[i]:
                
                break
        
        #print(l,r)

        return r -l +1
