def collectTheCoins(coins: List[int], edges: List[List[int]]) -> int:
    n = len(coins)
    tree = [set() for _ in range(n)]
    
    # Build the tree from the edges
    for e in edges:
        tree[e[0]].add(e[1])
        tree[e[1]].add(e[0])
    
    # Find the leaves with zero coins
    leaf = []
    for i in range(n):
        u = i
        while len(tree[u]) == 1 and coins[u] == 0:
            v = tree[u].pop()
            tree[v].remove(u)
            u = v
        if len(tree[u]) == 1:
            leaf.append(u)
    
    # Remove the leaves one by one
    for sz in range(2, 0, -1):
        temp = []
        for u in leaf:
            if len(tree[u]) == 1:
                v = tree[u].pop()
                tree[v].remove(u)
                if len(tree[v]) == 1:
                    temp.append(v)
        leaf = temp
    
    # Count the remaining edges in the tree
    ans = 0
    for i in range(n):
        ans += len(tree[i])
    
    return ans