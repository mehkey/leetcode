class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        
        arr1 = [nums[0]]
        
        arr2 = [nums[1]]

        N = len(nums)

        for i in range(2,N):
            
            if arr2[-1] < arr1[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1+arr2