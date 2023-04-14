class Solution:
    def minOperations(self, n: int) -> int:
        
        values = '0' + bin(n)[2:]
        
        m = float('inf')
        c = 0
        while int(values) != 0:
            
            #print(values)
            r = values[::-1]
            #r.reverse()
            #print('reve', r)
            
            for i,v in enumerate(r):
                if v == '1' and r[i+1] == '1': 
                    
                    values = '0' +bin(int(values, 2) + (1 << i))[2:]
                    c+=1
                    break
                elif v == '1' and r[i+1] == '0': 
                    
                    values = '0' +bin(int(values, 2) - (1 << i))[2:]
                    c+=1
                    break
                    
                    
        
        return c
        '''
        r = [[k,len(list(v))] for k,v in itertools.groupby(values)]
        
        s = str(values)
        
        o = 0
        p = 0
        
        for i,k in enumerate(r):
            if k[0] == '1' and (r[i-1][1] == 1):
                p += 1
            else:
                p += 2
                
        '''
        
        #print(r)
        return min(s.count("1"), p+1, s.count("0") + 2 )
        '''
        print(values)
        #print(bin(40))
        s = str(values)
        
        values = list(s)
        count = 0
        i = len(values)-1
        prev = False

        
        while i >= 0:
            if values[i] == '1':
                while i >= 0 and values[i] == '1':
                    i -=1
                    
                values[i] = '1'
                
                count+=1
            else:
                values[i] = '1'
                while i >= 0 and values[i] == '1':
                    i -=1

                count+=1
                #i-=1
        
        
        print(s.count("0") + 2 , s.count("1"), count )
        return min(s.count("0") + 2 , s.count("1"), count )
        '''


    
    def minOperations(self, n: int) -> int:
        res = 0
        while n > 0:
            if n % 2 == 0:
                n >>= 1
            elif (n & 2) > 0:
                n += 1
                res += 1
            else:
                res += 1
                n >>= 2
        return res