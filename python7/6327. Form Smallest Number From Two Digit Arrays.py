class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        
        '''m=min(nums1)
        n = min(nums2)
        
        if m == n:
            return m
        
        '''
        
        for i in range( 1 , 10):
            if i in nums1 and i in nums2:
                return i
        
        for f in range( 10 , 100):
            i = int(str(f)[0])
            j = int(str(f)[1])
            if i in nums1 and j in nums2:
                return f
            if i in nums2 and j in nums1:
                return f
        
        
            