class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        o = 0
        z = 0
        t = [i for i in str(s)]
        
        def check(t):
            for i in range(len(t)-1):
                if t[i] == '0' and t[i+1] == '1':
                    return False
            return True
        
        #print(t)
        c = 0
        while not check(t):
            i = 0
            while i < len(t)-1:
                if t[i] == '0' and t[i+1] == '1':
                    t[i], t[i+1] = t[i+1], t[i]
                    i+=1
                i+=1
            c+=1
            #print(t)
        return c
        
        
            
        #for c in str(s):
        #    if c == '1':
        #        o += 1
        #    if c == '0':
        #        z += 1
        
        #m = 0
        #for c in str(s)[::-1]:
        #    if m == '0':
        #        m+=1
        #    else:
        #        break
        
        #o = o - m
        #print(o)
        #print(z)
        #return (o - z)