class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        G = defaultdict(list)

        for e in edges:
            G[e[0]].append(e[1])
            G[e[1]].append(e[0])
        
        q = deque()
        q.append(source)
        v = set()
        while q:
            pop = q.popleft()
            if pop == destination:
                return True
            for n in G[pop]:
                if n not in v:
                    v.add(n)
                    q.append(n)
        
        return False