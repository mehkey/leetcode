class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
    	# Creating the undirected graph
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        # Use this counter to count how many time each node are used for all paths.
        count = Counter()
        # The totalCost if we don't reduce any node cost to half
        totalCost = 0
        # dfs to find the path from start node to end node.
        # Add the cost to total cost for each node on the path.
        # Also keep counting how many times each node are used for all paths in trips.
        # Since it is an undirected tree, even though there are no cycles, we can still travel back from the parent node. So keep the parent to avoid going backward of the tree.
        def dfs(node,par,end):
            nonlocal count
            nonlocal totalCost
            if node == end:
                return True
            
            for nei in graph[node]:
                if nei != par:
                    if dfs(nei, node, end):
                        count[nei] += 1
                        totalCost += price[nei]
                        return True
            return False

        # For each trip, we compute the path and update the totalCost, and count how many times each node is being used. 
        for start,end in trips:
            count[start] += 1
            totalCost += price[start]
            dfs(start,None,end)
        
        # The dp function to find the optimal combination of which node should be reduced.
        @cache
        def dp(node, par, canReduce):
            if canReduce:
                res = (price[node]//2)*count[node]
            else:
                res = 0
            red = 0
            for nei in graph[node]:
                if nei != par:
                	# if the cost of the current node can be reduced, we have only one option moving forward => do not reduce
                    if canReduce:
                        cur = dp(nei, node, False)
                    # if the cost of the current node can not be reduced, we have two options, either reduce it for the neighbor node or don't reduce it for the neighbor node.
                    else:
                        cur = max(dp(nei, node, False), dp(nei, node, True))
                    red += cur
            return res + red
        
        # We find the maximum reduction using the dp function.
        reduce = 0
        for i in range(n):
            reduce = max( reduce, dp(i, None, True), dp(i, None, False) )
        
        # reduce the total cost
        return totalCost - reduce
    

    class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        tree = [[] for _ in range(n)] 
        for u, v in edges: 
            tree[u].append(v)
            tree[v].append(u)
        freq = [0]*n
        for s, e in trips: 
            queue = deque([(s, -1)])
            parent = {s : -1}
            while queue: 
                u, p = queue.popleft()
                if u == e: break 
                for v in tree[u]: 
                    if v != p: 
                        queue.append((v, u))
                        parent[v] = u
            u = e 
            while u >= 0: 
                freq[u] += 1
                u = parent[u]
            
        def dfs(u, p):
            """Return """
            full = half = 0 
            for v in tree[u]: 
                if v != p: 
                    ff, hh = dfs(v, u)
                    full += ff
                    half += min(ff, hh)
            return price[u]*freq[u] + half, price[u]*freq[u]//2 + full
            
        return min(dfs(0, -1))