class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        """
        
        
        3 1 5 8 9 10 11
        
        
                        |
             |          |.   |.   | 
             3          1    5.   8
             | | | 
             1 5 8
             | |
             ...
             etc
             
        
        Permutation ( O(n!) )
        
        maxCount updated
        
        
        
        DP = 
        
        Window 
        DP 
        BFS X
        DFS X
        Heap X
             
        base case
        DP[(0,1)] = ...
        DP[(1,2)] = ...
        DP[(2,3)] = ...
        
        DP formula
        DP[(L,R)]  =  maximum( DP([L,L+1)] + DP[(L+1,R)] , DP([L,L+2)] + DP[(L+2,R)] ...)

        
        Space (O n ^2) n size of array
        Time  (O n ^3 )n size of array
        
        
        
        
        
        
        dp = {}
        
        newnums = [1] + nums + [1]
        #newnums.extend(nums)
        #newnums.append(1)
        
        nums= newnums
        #print(nums)
        
        def dfs(l,r):
            
            if l > r:
                return 0
            
            if (l,r) in dp:
                return dp[(l,r)]
            
            if l == r:
                total = nums[l]

                total *= nums[l-1]
                
                total *= nums[r+1]
                
                dp[(l,r)] = total
                
                return total
            
            dp[(l,r)] = 0
            
            #print(l, " ", r)
            
            for i in range(l,r+1):
                
                #print("num " , num)
                val = nums[l-1] * nums[i] * nums[r+1] 
                val += dfs(l,i-1) + dfs(i+1,r)
                #print(val)
                dp[(l,r)] = max(dp[(l,r)], val)
            
            #print("maximum ", l , " ", r, " is ", maximum)

            return dp[(l,r)]

        #dfs(1,len(nums)-2)

        #print(dp)
        
        return dfs(1,len(nums)-2)
        """
        ballons = nums
        
        length = len(ballons)
        dp = [[0 for j in range(length)] for i in range(length)]
        l = 0
        while l < length:
            i = 0
            while i + l < length:
                j = i + l
                leftBallon = ballons[i - 1] if i - 1 >= 0 else 1
                rightBallon = ballons[j + 1] if j + 1 < length else 1
                maxVal = -float('inf')
                for k in range(i, j + 1):
                    ksBurstCost = leftBallon * ballons[k] * rightBallon
                    if k == i:
                        # First in i <= k <= j
                        maxVal = max(maxVal, 0 + ksBurstCost + (dp[k + 1][j] if k + 1 < length else 0))
                    elif k == j:
                        # Last in i <= k <= j
                        maxVal = max(maxVal, dp[i][k - 1] + ksBurstCost + 0)
                    else:
                        # Mid in i <= k <= j
                        maxVal = max(maxVal, dp[i][k - 1] + ksBurstCost + dp[k + 1][j])
                dp[i][j] = maxVal
                i += 1
            l += 1
        return dp[0][length - 1]