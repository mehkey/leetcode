class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        
        
        """c = Counter(beans)
        
        hm = defaultdict(int)
        hm2 = defaultdict(int)
        total = sum(beans)
        
        l = len(beans)
        
        m = float("inf")
        for cc in c:
            #hm[cc] = total - cc*c[cc]
            #hm2[cc] = l - c[cc]
            
            total = 0
            
            for dd in c:
                if dd != cc:
                    total += (dd if dd < cc else min(dd,dd-cc)) * c[dd]
            
            #print('---')
            #print(cc)
            #print(total - cc*c[cc])
            #print((l -c[cc]) )
            #print(cc )
            #print(abs(total - cc*c[cc] -  (l -c[cc])*l ))
            #print(cc, total)
            m = min(m, total)
        
        return m
        """
        print(sorted(beans))
        print(sum(beans))
        print([a * (len(beans) - i) for i, a in enumerate(sorted(beans))])
        return sum(beans) - max(a * (len(beans) - i) for i, a in enumerate(sorted(beans)))
        
        


