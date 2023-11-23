class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        s1 = sum(nums1)
        s2 = sum(nums2)
        
        so = nums1.count(0)
        soo = nums2.count(0)
        
        r = 0
        
        s1 += so
        s2 += soo
        
        r += so
        r += soo
        
        if s1 == s2:
            return s1
        if s1 >= s2:
            if soo == 0:
                return -1
            
            return s1#r + s1 - s2
        if s2 > s1:
            if so == 0:
                return -1
            
            return s2 #r + s2 - s1
            