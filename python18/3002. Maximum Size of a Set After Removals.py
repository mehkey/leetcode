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

        '''
        while i < N or j < N:
            
            if i != N and j != N:
                if  nums1[i] <= nums2[j]:
                    #print(i,j)
                    if nums1[i] not in s:
                        c += 1
                        s.add(nums1[i])
                    i+=1
                elif nums2[j] <= nums1[i]:
                    if nums2[j] not in s:
                        c += 1
                        s.add(nums2[j])
                    j+=1
            if i == N:
                if nums2[j] not in s:
                    c += 1
                    s.add(nums2[j])
                j+=1
            if j == N:
                if nums1[i] not in s:
                    c += 1
                    s.add(nums1[i])
                i+=1

            if c == N :
                return len(s)
        
        return len(s)
        '''