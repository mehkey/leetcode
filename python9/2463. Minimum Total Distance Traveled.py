class Solution:
    def minimumTotalDistance(self, A: List[int], B: List[List[int]]) -> int:

        A.sort()
        B.sort(key=lambda x: x[0])

        '''
        @cache
        def dp(i,j,k):
            if i == len(robot):
                return 0

            if j == len(factory):
                return float('inf')

            if k == factory[j][1]:
                return dp(i,j+1,0)

            return min( dp(i,j+1,0) ,dp(i,j,k+1) + abs(robot[i]-factory[j][0]))

        return dp(0,0,0)
        '''

        @cache
        def dp(i, j, k):
            #print(i,j,k)
            if i == len(A): return 0
            if j == len(B): return float('inf')
            res1 = dp(i, j + 1, 0)
            res2 = dp(i + 1, j, k + 1) + abs(A[i] - B[j][0]) if B[j][1] > k else float('inf')
            m = min(res1, res2)

            return m

        return dp(0, 0, 0)