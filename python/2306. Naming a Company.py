class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        """
        s = set(ideas)

        l = len(ideas)

        res = set()

        for i in range(l-1):
            for j in range(i+1,l):
                
                w1 = ideas[i][0] + ideas[j][1:]
                w2 = ideas[j][0] + ideas[i][1:]
                
                if w1 in s or w2 in s:
                    pass
                else:
                    res.add(w1 + ' ' + w2)
                    res.add(w2 + ' ' + w1)
        
        return len(res)
        """
        
        hm = defaultdict(list)
        hm2 = defaultdict(list)
        hm3 = defaultdict(set)
        st = set()
        
        s = set(ideas)
        
        for w in s:
            #hm[w[1:]].append(w[0])
            #hm2[w[0]].append(w[1:])
            hm3[w[0]].add(w[1:])
            st.add(w[0])

        res = 0
        #print(hm2)
        
        """for i in hm2:
            for j in hm2:
                
                for v in hm2[i]:
                    for vv in hm2[j]:
                        w1 = i + vv 
                        w2 = j + v 
                        #print(w1 + ' ' + w2)
                        #s1 = ideas[i][0] + ideas[j][1:]
                        #s2 = ideas[j][0] + ideas[i][1:]
                        if w1 in s or w2 in s:
                            pass
                        else:
                            #print(w1 + ' ' + w2)
                            #print
                            #res.add(w1 + ' ' + w2)
                            #res.add(w2 + ' ' + w1)
                            res += 1

                #for k in st:
                #    for l in st:
                #        if ( k + 
                #        res += 1
        
        """
        #print(ord('a'))
        #print(1+ ord('a'))
        #print(chr(j + ord('a')))
        for a in range(25):
            for b in range(a+1,26):
                i = chr(a + ord('a'))
                j = chr(b + ord('a'))
                k = len(hm3[i] & hm3[j])
                res += 2 * ((len(hm3[i])- k) *(len(hm3[j])- k )) 
        
        
        return res
        #for k,v in hm.items():      
            
                
        