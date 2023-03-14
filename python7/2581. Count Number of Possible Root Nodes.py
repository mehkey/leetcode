class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:

        
        

        # Step 1 build the graph

        #contains all the edges
        # 0 -> 1,2,3 Node to list of Nodes
        GRAPH = defaultdict(list)

        #contains all the nodes
        NODES = set()

        for e in edges:

            NODES.add(e[0])
            NODES.add(e[1])

            GRAPH[e[0]].append(e[1])
            GRAPH[e[1]].append(e[0])

        ## Step 2 build a set of Guesses for fast access

        #contains all the guesses
        GUESSES = set()

        #contains all the edges of the nodes
        for e in guesses:
            GUESSES.add((e[0],e[1]))


        #visited set
        visited = set()

        # Step 3 DFS
        #cache the result with the node and previous
        @cache
        def dfs(node:int, previous:int) -> int:

            # count the number of right guesses
            guess_count = 0

            if (previous,node) in GUESSES:
                guess_count+=1

            # add node to visited set
            visited.add(node)

            for next_node in GRAPH[node]:

                if next_node not in visited:
                    guess_count += dfs(next_node,node)

            return guess_count
        
        # Step 4 Try all  the  roots

        result = 0

        for node in NODES:
            #if the root has k guesses, add 1 to the result
            if dfs(node,-1) >= k:
                result+=1
            visited = set()

        # Step 5 Return the result
        return result



class Solution:
    def rootCount(self, edges, guesses, k):
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        gt = set(map(tuple, guesses))

        @cache
        def dfs(i, par = None):
            return sum(((i, nextNode) in gt) + dfs(nextNode, i)
                       for nextNode in graph[i]
                       if nextNode != par)

        return sum(dfs(startNode) >= k for startNode in graph)