class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        
        res = []

        s = sorted(nums)

        n = len(nums)

        for i,num in enumerate(nums):
            
            c = 0
            
            v = set()
            for j in range(i+1,len(nums)):
                if nums[j] not in v:
                    c -=1
                    v.add(nums[j])
            v = set()
            for j in range(0,i+1):
                if nums[j] not in v:
                    c +=1
                    v.add(nums[j])

            res.append(c)

        return res
            