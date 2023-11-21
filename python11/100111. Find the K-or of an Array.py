class Solution:
    def findKOr(self, nums: List[int], kk: int) -> int:
        
        hm = defaultdict(int)
        
        for n in nums:
            c = 0
            while n:
                if n&1:
                    hm[c] += 1
                c += 1
                n = n >> 1
        r = 0
        #print(hm)
        for k,v in hm.items():
            if v >= kk:
                r += 1 << k
        return r
            #hm[]

