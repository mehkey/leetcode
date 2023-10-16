class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        G = defaultdict(list)
        for l,r in edges:
            G[l].append(r)
            G[r].append(l)

        def dfs(node,prev):
            tot = 0


            for n in G[node]:
                if n != prev:

                    c = count(n,node)

                    if c %k == 0:
                        tot += 1 + dfs(n,node)
                    else:
                        tot += dfs(n,node)

            return tot

        @cache
        def count(node,prev):
            
            tot = 0
            tot += values[node]

            for n in G[node]:
                if n != prev:
                    tot += count(n,node)
            
            return tot
        
        return dfs(0,-1) + 1
        