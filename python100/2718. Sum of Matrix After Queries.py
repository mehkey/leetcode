class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        
        r = defaultdict(tuple)
        c = defaultdict(tuple)

        co = 1
        
        #for i in range(n):
        #    r[i] = (0,0)
        #    c[i] = (0,0)

        rs = 0
        rsc = 0
        cs = 0
        csc = 0
        res = 0
        for t,i,v in queries[::-1]:
            #print(t,i,v)
            if t == 0:
                if i not in r:
                    r[i] = (v,co)
                    rsc += 1
                    rs += v
                    res += (v *(n-csc)) 

            if t == 1:
                if i not in c:
                    c[i] = (v,co)
                    csc += 1
                    cs += v
                    res += (v *(n-rsc)) 
 
            co+=1
        
        return res

        res = 0
        
        '''
        for i in range(n):
            for j in range(n):
                
                if r[i][1] > c[j][1]:
                    res += r[i][0]
                    #rr[i][j] = r[i][0]
                else:
                    res += c[j][0]
                    #rr[i][j] = c[j][0]
        '''
        #print(rr)
        return res
            