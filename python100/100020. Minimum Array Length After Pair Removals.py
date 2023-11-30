class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        
        #box = #itertools.iterator()
        m = 0
        
        t = 0
        
        nn = len(nums)

        kv= defaultdict(int)
        
        for n in nums:
            kv[n] += 1
            m = max(m, kv[n])
            
        #for key, gl in gg:
            #print(key,gl)
            #m = max(gl,m)
            #t += gl

        #if nn == 1:
        #    return 1

        if m > nn - m:
            #print('here' , nums)
            return m - nn + m

        #print(1%2)
        
        return 0 if nn % 2 == 0 else 1
