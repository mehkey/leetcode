class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], SS: int) -> List[int]:
        
        G = defaultdict(list)
        for l,r,v in edges:
            G[l].append((r,v))
            G[r].append((l,v))

            
        #@cache
        def dp( cur , prev, dist):
            
            r = defaultdict(int)
            
            r[dist % SS ] += 1
            #r.append(dist)

            for n,v in G[cur]:
                if n != prev:

                    acc = dp(n, cur, dist + v )

                    for a,v in acc.items():
                        #r.append( a)
                        r[a%SS] += v

            return r

        res = []
        
        for i in range(len(edges)+1):
            
            paths = []
            
            for n,v in G[i]:
                paths.append(dp(n,i, v))

            P = len(paths)

            c = 0
            for i in range(P):
                for j in range(i+1,P):
                    #print( paths[i][0] , paths[j][0])
                    c += paths[i][0] * paths[j][0]
                    #for p1 in paths[i]:
                    #    for p2 in paths[j]:
                    #        if p1 % signalSpeed == 0 and  p2 % signalSpeed == 0 :

                    #            c += 1
            res.append(c)
        return res
        