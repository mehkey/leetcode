class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        
        G = defaultdict(list)

        for e0,e1 in edges:
            G[e0].append(e1)
            G[e1].append(e0)

        @cache
        def dp(n, p, f):

            #m = 0

            ret = (coins[n] >> f) - k
            q = (coins[n] >> f + 1) 

            for nex in G[n]:
                if nex != p:
                    ret += dp(nex,n, min(f,14))
                    q += dp(nex,n, min(f+1,14))

            return max(ret,q)

        return dp(0, -1, 0)