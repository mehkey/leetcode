class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        res = 0

        for i in nums1:
            if len(nums2) %2 == 1:
                res ^= i 

        for j in nums2:
            if len(nums1) %2 == 1:
                res ^=  j 

        return res 