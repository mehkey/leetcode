#from segment_tree import SegmentTree
from sortedcontainers import SortedList

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        
        
        '''
        robot = sorted(robot)
        
        factory = sorted(factory, key = lambda x: x[0])
        
        N = len(factory)
        #print(robot)
        
        #print(factory)
        
        s = SortedList(factory)
        
        tot = 0
        
        for i,r in enumerate(robot):
            
            #print(s)
            #print(r)
            i = bisect.bisect_left(list(map(lambda x: x[0],s)), r)
            
            
            m = float('inf')
            
            #abs(s[i][0]-r)
            
            #ii = i
            
            
            
            if i+1 < len(s)  and abs(s[i+1][0]-r) < m:
                m = abs(s[i+1][0]-r)
                ii = i +1
                
            if abs(s[i][0]-r) < m:
                m = abs(s[i][0]-r)
                ii = i
                
            #if i-1 >= 0 and abs(s[i-1][0]-r) < m:
            #    m = abs(s[i-1][0]-r) 
            #    #m = min(m, abs(s[i]-r))
            #    ii = i-1

            tot += m
            ##print(ii)
            s[ii][1] -= 1
            
            if s[ii][1] == 0:
                s.pop(ii)
        
        return tot

        
        #from segment_tree import SegmentTree
 
 
        # an array with some elements
        #arr = [14, 28, 55, 105, 78, 4, 24, 99, 48, 200]
        #t = SegmentTree(arr)
        
        #a = t.query(float('-inf'), float('inf'), "min")
        #print("The minimum value of this range is : ", a)
        
        
        '''
        A = robot
        B = factory
        A.sort()
        B.sort()
        @lru_cache(None)
        def dp(i, j, k):
            #print(i,j,k)
            if i == len(A): return 0
            if j == len(B): return float('inf')
            res1 = dp(i, j + 1, 0)
            res2 = dp(i + 1, j, k + 1) + abs(A[i] - B[j][0]) if B[j][1] > k else float('inf')
            m = min(res1, res2)
            #print(m)
            return m
        return dp(0, 0, 0)
        
        
        A = robot
        B = factory
        A.sort()
        B.sort()
        n, m = len(A), len(B)
        dp = [inf] * (n + 1)
        dp[n] = 0
        #A.sort()
        #B.sort()
        for j in range(m-1,-1,-1):
            print(dp)
            for i in range(n):
                cur = 0
                for k in range(1, min(B[j][1], n - i) + 1):
                    cur += abs(A[i + k - 1] - B[j][0])
                    dp[i] = min(dp[i], dp[i + k] + cur)
        print(dp)
        return dp[0]

