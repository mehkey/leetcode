class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = [0,0]
        s1 = set(nums1)
        s2 = set(nums2)
        for n in nums1:
            if n in s2:
                res[0]+=1
        for n in nums2:
            if n in s1:
                res[1]+=1
        return res
        