class Solution:
    def maximizeWin(self, A: List[int], k: int) -> int:
        
        dp = [0] * (len(A) + 1)
        res = 0
        j = 0
        
        
        for i, a in enumerate(A):
            #print(dp)
            while A[j] < A[i] - k: j += 1
            dp[i + 1] = max(dp[i], i - j + 1)
            res = max(res, i - j + 1 + dp[j])
        return res

def maximizeWin(self, arr: List[int], k: int) -> int:
        n = len(arr)
        best = [0]*(n+1)  # best segment after >= i 
        res = 0
        for i in range(n-1,-1,-1):   # curr seg start at ith
            e = bisect.bisect_right(arr,arr[i]+k)   # take maximum as possible
            res = max(res,e-i + best[e])  # maximize the segments by curr seg + next segment after >= e
            best[i] = max(best[i+1],e-i)  # track the best segment
        return res