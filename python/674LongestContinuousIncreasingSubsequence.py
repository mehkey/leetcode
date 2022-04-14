class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        curLongest = 1
        maxLongest = 1
        for i in range(1,len(nums)):

            if(nums[i] > nums[i-1]):
                curLongest += 1
                maxLongest = max(maxLongest,curLongest)
            else:
                curLongest = 1

        return maxLongest