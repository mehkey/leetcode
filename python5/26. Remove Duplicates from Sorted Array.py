class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        #for i,n in enumerate(nums,start = 1):
        #    print(i,n)
        #j = 0
        N = len(nums)
        j = N -1

        #for i in range(len(nums)-1):
        #    if nums[i] == nums[i+1]:
                #nums[i+1] = nums[i+2]

        '''
        for i in range(len(nums)-1,0,-1):

            if nums[i] != nums[i-1]:
                #nums[j] = nums[i]

                nums[i] = nums[j]
                nums[j] = None
                j -= 1
        '''
        k = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:            # detect next unique value 
                nums[k] = nums[i]               # move it to the end of deduplicated array
                k += 1                          # update the size of deduplicated array

        return k
