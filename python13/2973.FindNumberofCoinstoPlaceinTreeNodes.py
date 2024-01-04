from sortedcontainers import SortedList

class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        
        #print(edges)
        G = defaultdict(list)
        
        res = [0]*len(cost)

        for l,r in edges:
            G[l].append(r)
            G[r].append(l)

        
        def dfs(node,prev,ol):
            
            if size(node,prev) == 1:
                #print('here', node)
                ol.add(cost[node])
                res[node] = 1
                return
            
            pos = []
            
            sl = SortedList()

            for n in G[node]:
                if n != prev:
                    dfs(n,node,sl)
            
            sl.add(cost[node])

            if len(sl) < 3:

                res[node] = 1
            if len(sl) >= 3:
                a1 = sl[-1] * sl[-2] * sl[-3]
                a2 = sl[0] * sl[1] * sl[-1]
                res[node] = max(a1, a2,0)
            
            
            ol.update(sl)


        @cache
        def size(node,prev):
            
            if len(G[node]) == 1 and prev != -1:
                return 1

            tot = 0

            for n in G[node]:
                if n != prev:
                    tot+=size(n,node)

            return tot + 1
        
        #from sortedcontainers import SortedList
        sl = SortedList()

        dfs(0,-1,sl)
        
        return res