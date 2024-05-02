class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(profit)
        arr = sorted(zip(startTime,endTime,profit))
        arr2 = list(sorted(startTime))

        @cache
        def dp(i):
            
            if i >= N:
                return 0
            
            res = dp(i+1)

            cur = bisect.bisect_left(arr2, arr[i][1] )

            res = max(res, dp(cur)  + arr[i][2])

            return res

        return dp(0)
    

