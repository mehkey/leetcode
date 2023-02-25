class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        """
        
        days = [1,4,6,7,8,20], costs = [2,7,15]
        
        
                                  |
                                 day 1
                | 1day  $c1        |  7 day $C2      | 30 day $C3
                day 2             day 8               day 31
            |.  |.  |             | | |            | | |
               day 8
            ...etc.                .etc
        
        day0 = 0
        day1 = C1
        
        dp[day] = min( C3*dp[day-30] , C2*dp[day-7])
        
        DFS > 30 
        DFS > 7
        
        
        
        dp[(start,end)] = min( dp[start,i] +  dp[i,end])
        
        dp[] # index of the last element in days array
            
        

        if len(days) == 0:
            return 0

        dp = {}
        dp[(0,0)] = 0  
        
        
        def dfs(start,end):
            
            if (start,end) in dp:
                return dp[(start,end)]
            
            if end - start + 1 < 7:
                val = ( end - start + 1 ) % 7 * costs[0]
                dp[(start,end)] = val
                return val
            
            minimum = float("inf")
            
            for i in range(max(start,end-30),end):
                range1 = (start,i)
                range2 = (i,end)
                
                dfs(range1[0],range1[1])
                
                minimum = min(minimum, dp[range1] + costs[2])
            
            for i in range(max(start,end-7),end):
                range1 = (start,i)
                range2 = (i,end)
                
                dfs(range1[0],range1[1])
                
                minimum = min(minimum,dp[range1] + costs[1])
            
                
            dp[(start,end)] = minimum
            
            return dp[(start,end)]

        dfs(days[0],days[-1])
        
        return dp[(days[0],days[-1])]

        
        


        if len(days) == 0:
            return 0

        dp = {}

        dp[len(days)-1] = min(costs[0],costs[1],costs[2])
        
        def dfs(dayIndex):

            if dayIndex == len(days):
                return 0
            
            if dayIndex in dp:
                return dp[dayIndex]
            
            minimum = sys.maxsize
              
            #    dfs()
            #    minimum = min(minimum, dp[range1] + costs[2])
            #    DP[day10] DP[day11]
            #.   DP[day4]
            
            minimum = min(minimum, costs[0] + dfs(dayIndex + 1) )
            minimum = min(minimum, costs[1] + dfs(dayIndex + 1) )
            minimum = min(minimum, costs[2] + dfs(dayIndex + 1) )
            
            #for i in range(dayIndex + 1, len(days)):
            for i in range( len(days)-1, dayIndex + 1, -1):    
                if days[i] - days[dayIndex] < 30:
                    minimum = min(minimum, costs[2] + dfs(i+1) )
                    break
                    
            for i in range( len(days)-1, dayIndex + 1, -1): 
                if days[i] - days[dayIndex] < 7:
                    minimum = min(minimum, costs[1] + dfs(i+1) )
                    break

            dp[dayIndex] = minimum
            return  dp[dayIndex]
            
        return dfs(0)
        
        
        """
    
        if len(days) == 0:
            return 0

        dp = {} #

        dp[len(days)-1] = min(costs[0],costs[1],costs[2])
        
        for dayIndex in range(len(days)-2,-1,-1):
            
            minimum = sys.maxsize
              
            #    dfs()
            #    minimum = min(minimum, dp[range1] + costs[2])
            #    DP[day10] DP[day11]
            #.   DP[day4]
            
            minimum = min(minimum, costs[0] + dp[dayIndex + 1] )
            minimum = min(minimum, costs[1] + dp[dayIndex + 1] )
            minimum = min(minimum, costs[2] + dp[dayIndex + 1] )
            
            #for i in range(dayIndex + 1, len(days)):
            #print(dayIndex)
            for i in range( len(days)-1, dayIndex + 1, -1):
                #print(i)
                #print(len(days)-1)
                if days[i] - days[dayIndex] < 30:
                    minimum = min(minimum, costs[2] + (dp[i +1] if i +1 <len(days) else 0))
                    break
                    
            for i in range( len(days)-1, dayIndex + 1, -1): 
                if days[i] - days[dayIndex] < 7:
                    minimum = min(minimum, costs[1] + (dp[i +1] if i +1 <len(days) else 0))
                    break

            dp[dayIndex] = minimum
            #return  dp[dayIndex]
            
        return dp[0]
    

        
        
        