class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        
        s = set()
        
        N = len(nums1)

        s1 = set(nums1)
        s2 = set(nums2)
        
        u1 = s1  -s2
        u2 = s2 - s1

        shared = s1 & s2

        return min( min(len(u1), N//2) + min(len(u2), N//2) + len(shared), N )


