class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        arr1 = [0] * (len(nums)//2)
        arr2 = [0]* (len(nums)//2)
        
        i,j,k = 0,0,0
        
        res = [0] * len(nums)

        for n in nums:
            if nums[i] >0:
                arr1[j] = nums[i]
                j+=1
            else:
                arr2[k] = nums[i]
                k+=1
            i+=1 
        i,j,k = 0,0,0
        while i<len(nums):
            
            if i%2 == 0:
                res[i] = arr1[j]
                j+=1

            if i%2 == 1:
                res[i] = arr2[k]
                k+=1
            i+=1
        
        return res