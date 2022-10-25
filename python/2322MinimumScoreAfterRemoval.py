class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        """
        #@cache
        def dfs(i, j):
            X, x = [], nums[j]
            for k in adj[j]:
                if k == i: continue
                X += dfs(j, k)
                x ^= X[-1]
            X.append(x)
            return X

        res, adj = math.inf, [[] for _ in range(len(nums))]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        for i, j in edges:
            X, Y = dfs(i, j), dfs(j, i)
            print(X)
            print(Y)
            for X, Y in (X, Y), (Y, X):
                for x in X[:-1]:
                    y = X[-1] ^ x
                    res = min(res, max(x, y , Y[-1]) - min(x, y, Y[-1]))
        return res
        

        s = reduce(lambda x,y:x^y, nums)
        adj = defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        self.res = float('inf')
        
        def calc_res(a,b,c):
            return max(a,b,c) - min(a,b,c)
        
        def dfs(root,parent,others):
            subtrees = set()
            cur = nums[root]
            for i in adj[root]:
                if i!=parent:
                    v, children = dfs(i,root,others|subtrees)
                    subtrees |= children
                    cur ^= v
			
            for other in others:
                self.res = min(self.res,calc_res(cur,i,s^cur^other))
            if parent!=-1:
                for child in subtrees:
                    self.res = min(self.res,calc_res(cur^child,s^cur,child))
            subtrees.add(cur)
            return cur,subtrees
        
        dfs(0,-1,set())
        
        return self.res
        
        
        
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v in edges: 
            graph[u].append(v)
            graph[v].append(u)
            
        def fn(u): 
            score[u] = nums[u]
            child[u] = {u}
            for v in graph[u]: 
                if v not in seen: 
                    seen.add(v)
                    fn(v)
                    score[u] ^= score[v]
                    child[u] |= child[v]
        
        seen = set()
        score = [0]*n
        child = [set() for _ in range(n)]
        fn(0)
        print(score)
        print(child)
        ans = inf 
        for u in range(1, n): 
            for v in range(u+1, n): 
                if u in child[v]: 
                    uu = score[u]
                    vv = score[v] ^ score[u]
                    xx = score[0] ^ score[v]
                elif v in child[u]: 
                    uu = score[u] ^ score[v]
                    vv = score[v]
                    xx = score[0] ^ score[u]
                else: 
                    uu = score[u]
                    vv = score[v]
                    xx = score[0] ^ score[u] ^ score[v]
                ans = min(ans, max(uu, vv, xx) - min(uu, vv, xx))
        return ans  
        
        
        """
        
        find = defaultdict(list)
        for x, y in edges:
            find[x].append(y)
            find[y].append(x)

        @cache
        def get_xors_of_subtree(root, prev):
            res = []
            val = nums[root]
            for y in find[root]:
                if y != prev:
                    tmp = get_xors_of_subtree(y, root)
                    res.extend(tmp)
                    val ^= tmp[-1]
            res.append(val)
            return res

        res = math.inf
        for x, y in edges:
            left_xors = get_xors_of_subtree(x, y)
            right_xors = get_xors_of_subtree(y, x)
            left_val = left_xors[-1]
            right_val = right_xors[-1]
            for l1 in left_xors[:-1]:
                l2 = left_val ^ l1
                res = min(res, max(l1, l2, right_val) - min(l1, l2, right_val))
            for r1 in right_xors[:-1]:
                r2 = right_val ^ r1
                res = min(res, max(r1, r2, left_val) - min(r1, r2, left_val))