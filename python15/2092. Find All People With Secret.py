class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        
        graph = defaultdict(list)

        for x,y,t in meetings:
            graph[x].append((y,t))
            graph[y].append((x,t))

        heap = [(0,firstPerson)] #time,person
        for nei,time in graph[0]:
            heapq.heappush(heap,(time,nei))
        
        visited = set([0])

        while heap:
            time,person = heapq.heappop(heap)

            if person in visited:
                continue

            visited.add(person)

            for nei,t in graph[person]:
                if t>=time:
                    heapq.heappush(heap,(t,nei))

        return visited
        
        meetings.sort(key=lambda x: x[2])

        d = deque(meetings)        
        
        s = set()
        s.add(0)
        s.add(firstPerson)

        t = 0
        
        while d:
            
            G = defautldict()
            while d and d[0][2] <= t:
                
                x,y,t = d.popleft()
                
                if x in s:
                    s.add(y)
                if y in s:
                    s.add(x)
                lis.append([x,y])
            
            for x,y in lis:
                if x in s:
                    s.add(y)
                if y in s:
                    s.add(x)

            t += 1
        
        return list(s)
        
        
        