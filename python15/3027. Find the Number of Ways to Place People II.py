class Solution:
    def numberOfPairs(self, p: List[List[int]]) -> int:

        N = len(p)

        res = 0

        p.sort(key=lambda x: (x[0],-x[1]))

        for i in range(N):

            minLeft = -inf

            for j in range(i+1,N):

                if  p[i][1] >= p[j][1] and p[j][1] > minLeft:
                    res += 1
                    minLeft = max(p[j][1] , minLeft)

        return res
