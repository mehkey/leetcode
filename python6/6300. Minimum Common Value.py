class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        s1 = set(nums1)
        
        s2 = set(nums2)
        
        s3 = s1.intersection(s2)
        
        if len(s3) == 0:
            return -1
        else:
            return min(s3)