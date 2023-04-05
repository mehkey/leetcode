class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        
        answer = maxsize
        
        G = defaultdict(list)
        
        for e in edges:
            G[e[0]].append(e[1])
            G[e[1]].append(e[0])
 
        for i in range(n):

            distance = [float('inf')] * n

            parent = [-1] * n

            distance[i] = 0
            q = deque()

            q.append(i)

            while q:

                x = q[0]
                q.popleft()

                for child in G[x]:

                    if distance[child] == float('inf'):

                        distance[child] = 1 + distance[x]

                        parent[child] = x

                        q.append(child)

                    elif parent[x] != child and parent[child] != x:
                        answer = min(answer, distance[x] +
                                       distance[child] + 1)

        if answer == maxsize:
            return -1

        return answer