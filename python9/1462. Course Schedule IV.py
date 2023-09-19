class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = collections.defaultdict(list)
        r_graph = collections.defaultdict(list)
        ancestor = [set() for i in range(numCourses)]
        for a, b in  prerequisites:
            graph[a].append(b)
            r_graph[b].append(a)

        queue = []
        for i in range(numCourses):
            if not r_graph[i]:
                queue.append(i)

        while queue:
            node = queue.pop(0)
            for v in graph[node]:
                ancestor[v].add(node)
                ancestor[v].update(ancestor[node])
                r_graph[v].remove(node)
                if not r_graph[v]:
                    queue.append(v)

        ans = []
        for a, b in queries:
            if a in ancestor[b]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
