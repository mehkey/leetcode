class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        
        
        '''
        def dfs(node,v,s):
            nonlocal m
            
            if node in v or node == s:
                return 0

            if vals[node] > vals[s]:
                return 0

            tot = 0

            if vals[node] == vals[s]:
                tot += 1

            v.add(node)

            for nex in m[node]:
                tot += dfs(nex,v,s)

            return tot

        res = len(vals)
        
        m = defaultdict(list)
        
        for e in edges:
            m[e[0]].append(e[1])
            m[e[1]].append(e[0])

        res2 = 0
        for node in range(len(vals)):
            visited = set()
            for nex in m[node]:
                res2 += dfs(nex,visited,node)

        return res + (res2 //2)
        
        '''
        
        res = n = len(vals)
        f = list(range(n))
        count = [Counter({vals[i]: 1}) for i in range(n)]
        edges = sorted([max(vals[i], vals[j]),i,j] for i,j in edges)

        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        for v,i,j in edges:
            fi, fj = find(i), find(j)
            cj, ci = count[fi][v], count[fj][v]
            res += ci * cj
            f[fj] = fi
            count[fi] = Counter({v: ci + cj})
        return res
            