class Solution:
    def minimumOperations(self, n: List[int]) -> int:
        if len(n) == 1 or len(n) == 0:
            return 0
        
        e1 = [n[i] for i in range(0,len(n),2) ]
        o1 = [n[i] for i in range(1,len(n),2) ]
        
        l1 = len(e1)
        
        l2 = len(o1)
        
        c1 = Counter(e1 )
        c2 = Counter(o1 )

        #print(c1)
        #print(c2)
        #print(e1)
        #print(o1)

        d1 =  max(c1, key=c1.get) 
        v1 = max(c1.values())
        
        d2 =  max(c2, key=c2.get)
        v2 = max(c2.values())
        
        #print(d1)
        #print(d2)
        
        if d1 == d2 :
            del c1[d1]
            del c2[d2]
            #print(max(c1.values()) if c1 else 0)
            #print(max(c2.values()) if c2 else 0)
            #print(l1)
            ##print(l2)
            #print(l2 - v2 + l1 - (max(c1.values()) if c1 else 0))
            #print(l1 - v1 + l2 - (max(c2.values()) if c2 else 0 ))
            
            return min( l2 - v2 + l1 - ( max(c1.values()) if c1 else 0), l1 - v1 + l2 - (max(c2.values()) if c2 else 0)  )
            
        else:
            return  l1 - v1 + l2- v2
        
        
        #if d1 / len() 
        
        #if del counter_dict[key]
        
        #if 
        #key=ages.get)
        

class Solution:
    def minimumOperations(self, n: List[int]) -> int:
        if len(n) == 1 or len(n) == 0:
            return 0
        
        e1 = [n[i] for i in range(0,len(n),2) ]
        o1 = [n[i] for i in range(1,len(n),2) ]
        
        l1 = len(e1)
        
        l2 = len(o1)
        
        c1 = Counter(e1 + [0] )
        c2 = Counter(o1 + [0] )

        d1 =  max(c1, key=c1.get) 
        v1 = max(c1.values())
        
        d2 =  max(c2, key=c2.get)
        v2 = max(c2.values())

        if d1 == d2 :
            del c1[d1]
            del c2[d2]

            return min( l2 - v2 + l1 - ( max(c1.values()) ), l1 - v1 + l2 - (max(c2.values()) )  )
            
        else:
            return  l1 - v1 + l2- v2
        