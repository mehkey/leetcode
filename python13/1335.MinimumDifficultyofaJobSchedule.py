class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        M = len(jobDifficulty)

        @cache
        def dp(i, b, curm):
            if i == M:
                if b != d or curm != -1  :
                    return inf
                else:
                    return 0
            


            res = inf
            cd = jobDifficulty[i]

            if curm == -1:
                return min(res, dp(i+1, b, cd ) , dp(i+1, b+1, -1 ) + cd)

            else:

                res = min(res, dp(i+1, b,  max(curm, cd)) )

                res = min(res, dp(i+1, b + 1, -1 ) + max(curm, cd)  )

                return res
        
        res =  dp(0,0, -1)

        return res if res != inf else -1