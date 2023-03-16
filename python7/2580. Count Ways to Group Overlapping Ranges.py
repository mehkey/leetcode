class Solution:
    def countWays(self, r: List[List[int]]) -> int:
        
        g = 0
        
        r.sort(key=lambda x: x[0])

        c = 0

        prev = -1

        for i in range(len(r)):

            if r[i][0] > prev:
                c += 1
                prev = r[i][1]

            else:
                prev = max(r[i][1],prev)

        return pow(2,c,10**9+7)
