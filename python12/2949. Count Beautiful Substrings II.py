class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        
        
        md = set()
        for i in range(k):
            if i*i%k == 0:
                md.add(i)
        
        diff = {0: {0: 1}}
        d = 0
        v = 0
        ret = 0
        for x in s:
            if x in 'aeiou':
                d += 1
                v += 1
            else:
                d -= 1
            if d in diff:
                #for q in md:
                dd = diff[d]
                
                    #if (v-q)%k in diff[d]:
                for q in md:
                    ret += dd.get((v-q)%k,0)#diff[d][(v-q)%k]
            else:
                diff[d] = {}
            diff[d][v%k] = diff[d].get(v%k, 0) + 1
        return ret


        c = 0
        v= 0
        n = len(s)
        r = 0
        
        kd = defaultdict(int)
        
        #vch = defaultdict(list)
        vch = defaultdict(list)
        
        vcc = defaultdict(int)
        #vch[0].append((0,0))
        
        '''
        
        baeyh
        
        b (1)

        bae     (check (2-1,1)  mod 2 is bad)
        (2,1)
        
        baey   (check (2,2)  YES)
        (2,2)  
        
        baeyh  (check 3-1,2 mod 2 YES)
        (3,2)
        '''
        
        marks = []
        res = 0
        
        # 1 2 3 
        for r in range(n):
            

            if s[r] in 'aeiou':
                c+=1
            else:
                v+=1
            
            #vch[v-c].append((c,v))

            #prev[(v * c) % k] +=  
            
            
            if c - v == 0:
                #print("PERFECT", r, c,v)
                #print(s[0:r+1])
                
                if c == v and (c*v) % k == 0:
                    #print(' YES')
                    res += 1
            
            if c - v in vcc:
                res +=  vcc[c - v]
                
            #if c - v in vch:
                
                
                #print(s[0:r+1])
                #print(c,v)
                #print(vch)
                #for cur in marks
                
                #kd[(v*c)%k] += 1
                
                #if 
                
                #if cc,vv in vcc[c - v]:
                #    res +=  vcc[c - v]
                
                '''
                for cc,vv in vch[c - v]:
                    #print("!!", vch[c - v])
                    ccc = c-cc
                    vvv = v-vv
                    #print("ccc",ccc,vvv)

                    if ccc == vvv and (ccc*vvv) % k == 0: 
                        #print('AND YES')
                        #res += vch[c-v] 
                        res += 1

                    #kd[(v*c)%k]
                '''
                #marks.append(r)
            
                #print(marks, v,c)

                #print(kd, v,c, v*c, (v*c)%k)
            
            #elif c-v == 0:
            #    res += 1
            #if c == k or v == k:
            #    vch[c-v] += 1
            
            if c >= k or v >= k:
                vcc[c-v]+=1
            #vch[c-v].append((c,v))

            #if v == c and (v * c) % k == 0:
            #r += 1
        
        return res