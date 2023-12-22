class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        l = 0

        #ml,mr = -1,-1
        m = 0
        #hm = set()
        hm = defaultdict(int)
        for r in range(n):
            
            if s[r] in hm:
                val = hm[s[r]]#s[l]

            #while l < n and s[r] in hm:

                #del hm[s[r]]
                #hm.remove(s[l])
                l = max(val + 1,l)
                
            #hm.add( s[r])
            hm[s[r]] = r
            print(l,r)
            m = max(m, r - l + 1)

            #m = max(m, r - l + 1)
        
        return m