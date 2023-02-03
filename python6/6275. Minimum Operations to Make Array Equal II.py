class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        '''
        d1 = defaultdict(list)
        d11 = defaultdict(int)
        
        for n in nums1:
            d1[n%k].append(n)
            d11[n%k] += n//k
        
        d2 = defaultdict(list)
        d22 = defaultdict(int)
        for n in nums2:
            d2[n%k].append(n)
            d22[n%k] += n//k
            
        #print(d1,d2)
        #print(d11,d22)
        
        if d11 == d22:
            return 
        '''

        if k == 0:
             return 0 if nums1 == nums2 else  -1
            
        count = 0
        total = 0
        for i,n in enumerate(nums1):
            
            if nums1[i]%k != nums2[i] %k:
                return -1
            
            diff = nums1[i] - nums2[i]
            
            count += diff // k
            total += abs( diff // k)
            
        
        if count == 0:
            return total //2
        
        return -1
        