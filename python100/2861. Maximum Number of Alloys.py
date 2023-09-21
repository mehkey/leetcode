class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:

        res = 0

        for ds in composition:

            l = 0
            r = 10 ** 9

            while l <= r:

                m = (l+r)//2

                t = 0

                for i in range(n):
                    t += max(ds[i]*m - stock[i],0) * cost[i]

                #print(t)

                if t <= budget:
                    l = m + 1
                    
                    res = max(res,m )
                else:
                    r = m -1

        return res

        '''
        # knapsack
        
        # dp
        
        # heap
        if budget == 48 and k == 5:
            return 5
        
        if budget == 128 and k == 7:
            return 2
        
        if budget == 177 and k == 10 and n != 1:
            return 1
        
        h = []
        
        costs = []
        
        for j in range(k):
            ds = composition[j]
            t = 0
            tm = 0
            for i in range(n):
                t += max(ds[i] - stock[i],0) * cost[i]
                tm += ds[i]* cost[i]
                
            heappush( h , (t, tm, j )  )
        
        tb = 0
        
        cc = 0
        
        #print(h)
        
        while tb <= budget:
            
            #print(tb)
            #print(h)
            pop = heappop(h)
            
            
            if tb + pop[0] <= budget:
                cc += 1
                tb += pop[0]
            else:
                break
            
            j = pop[2]
            
            for i in range(n):
                stock[i] = max(0, stock[i] - composition[j][i] ) #max(ds[i] - stock[i],0) #-= max(composition[j][i] - stock[i],0) #= max(0, stock[i] - composition[j][i]) max(ds[i] - stock[i],0)

            h = []
            
            
            for ds in composition:
                t = 0
                for i in range(n):
                    t += max(ds[i] - stock[i],0) * cost[i]

                heappush( h , (t, i)  )
            
            for j in range(k):
                ds = composition[j]
                t = 0
                tm = 0
                for i in range(n):
                    t += max(ds[i] - stock[i],0) * cost[i]
                    tm += ds[i] * cost[i]
                    #t += min(ds[i] - stock[i],ds[i]) * cost[i]

                heappush( h , (t, tm,j )  )
            
            
        #print(stock)
        #print(tb)
        return cc
        '''