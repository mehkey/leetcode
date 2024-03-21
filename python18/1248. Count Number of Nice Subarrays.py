class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        r = 0
        l = 0
        N = len(nums)
        oc =0
        
        t = 0
        #print(' ')
        while r < N:
            
            if nums[r] %2 == 1:
                oc += 1
            nr = r + 1
            while nr < N and nums[nr] %2 != 1:
                nr += 1
                
            #print(oc, nr)
            while l <= r and oc == k:
                t += nr - r
                #print('plus', nr - r)
                if nums[l] %2 == 1:
                    oc -= 1
                
                l += 1
            r += 1
        return t