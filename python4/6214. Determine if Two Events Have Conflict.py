class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        def t(tt):
            tt = tt.split(':')
            return time(int(tt[0]),int(tt[1]))
        

        t1 = t(event1[0])
        t2 = t(event1[1]) 
        t3 = t(event2[0]) #time(time3[0],time3[1])
        t4 = t(event2[1]) #time(time4[0],time4[1])
        
        #x = range(int(t1),int(t2))
        #y = range(int(t3),int(t4))
        #result = list(set(x) & set(y))
        
        #return len(result) > 0
        
        return (t1 <= t3 and t2 >= t3)   or  ( t3 <= t1 and t4 >= t1) 