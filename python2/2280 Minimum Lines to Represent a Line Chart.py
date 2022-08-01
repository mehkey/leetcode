class Solution:
    def minimumLines(self, A: List[List[int]]) -> int:
        
        """
        lines = 0
        
        prev = (1000,1000)
        
        #print(len(sp))
        sp = sorted(sp)
        prevs = math.floor(sp[1][1] - sp[0][1]   / sp[1][0] - sp[0][0] * 10000)
        for i in range(1,len(sp)):
            o = sp[i]
            x = o[0]
            y = o[1]
            dx = x - prev[0]
            dy = y - prev[1]
            
            s = math.floor(dy / dx * 10000)
            
            #print(prevs,s)
            if s != prevs:
                lines+=1
                #print("C")
            else:
                #print("HERE")
                pass
            
            prevs = s
            prev = (x,y)
            #print(lines)
            
        #print(lines)
        return lines 
        
        n = len(stockPrices)
        stockPrices.sort(key = lambda x: (x[0], x[1]))
        
        if n == 1:
            return 0
        
        pre_delta_y = stockPrices[0][1] - stockPrices[1][1]
        pre_delta_x = stockPrices[0][0] - stockPrices[1][0]
        num = 1
        
        for i in range(1, n-1):
            cur_delta_y = stockPrices[i][1] - stockPrices[i+1][1]
            cur_delta_x = stockPrices[i][0] - stockPrices[i+1][0]
            
            if pre_delta_y * cur_delta_x != pre_delta_x * cur_delta_y:
                num += 1
                pre_delta_x = cur_delta_x
                pre_delta_y = cur_delta_y
        
        return num
        """
        A.sort() # to bring consecutive points on graph together
        n=len(A)
                
        # calculate if three points lie on the same line        
        is_same_line = lambda a,b,c: (b[0]-a[0])*(c[1] - b[1])==(c[0]-b[0])*(b[1] - a[1])
        
        return n - 1 - sum(is_same_line(A[i-1], A[i], A[i+1]) for i in range(1, n-1) )