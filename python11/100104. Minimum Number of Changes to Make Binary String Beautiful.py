class Solution:
    def minChanges(self, s: str) -> int:
        
        ce = 0
        
        cur = 0
        count = 0
        
        it = groupby(s)
        
        res = [(sum(1 for x in v)) for k,v in it]
        
        i = 0
        while i < len(res):
            v = res[i]
            if v %2 == 0:
                i += 1
            elif v %2 == 1 and i+1 < len(res) and res[i+1] %2 == 1:
                ce += 1

                i+= 2
            else:
                ce += 1
                
                if i+1 < len(res):
                    res[i+1] += 1
                else:
                    ce += 1
                
                i+= 1

        return ce
        '''
        for k,v in it:
            vv = sum(1 for x in v)
            if  vv  % 2 == 1:
                ce += 1
            #print(k,vv)
        #print(ce)
        return ceil(ce)
        
        for c in s:
            if c == '0':
                
                if cur == '0':
                    count += 1
            
            if c == '1':
        '''   
        
        #return 0