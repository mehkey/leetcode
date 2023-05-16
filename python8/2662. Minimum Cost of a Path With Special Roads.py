class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:

        m = min(start[0],target[0])
        M = max(start[0],target[0])
        N = max(start[1],target[1])
        n = min(start[1],target[1])

        h = []

        h.append((0,(start[0],start[1])))

        dirs = ((0,1),(1,0),(-1,0),(0,-1))
        v = set()
        v.add((start[0],start[1]))

        sr = defaultdict(list)

        for r in specialRoads:
            #sr[(r[0],r[1])].append((r[2],r[3],r[4]))
            heappush(h, ( abs(start[0]-r[0]) + abs(start[1]-r[1]) + r[4],(r[2],r[3])))

        #if (start[0],start[1]) in sr:
            #vv = sr[(start[0],start[1])]
            #v.add((vv[0],vv[1]))
            #for vv in sr[(start[0],start[1])]:
                #heappush(h, (0 + vv[2],(vv[0],vv[1])))

        heappush(h, (abs(start[0]-target[0]) + abs(start[1]-target[1]),(target[0],target[1])))

        #print(h)

        while h:

            dis, pos = heappop(h)

            if pos[0] == target[0] and pos[1] == target[1]:
                return dis

            '''
            if (pos[0],pos[1]) in sr:
                for vv in sr[(pos[0],pos[1])]:
                    heappush(h, (dis + vv[2],(vv[0],vv[1])))
            '''

            #for r in specialRoads:

                #heappush(h, ( dis + abs(pos[0]-r[0]) + abs(pos[1]-r[1])  + r[4],(r[2],r[3])))

            heappush(h, (dis+abs(pos[0]-target[0]) + abs(pos[1]-target[1]),(target[0],target[1])))

            '''
            for d in dirs:
                nx= pos[0] + d[0]
                ny = pos[1] + d[1]

                if m <= nx <= M and n <= ny <= N and (nx,ny) not in v:
                    v.add((nx,ny))
                    heappush(h, (dis + 1,(nx,ny)))
            '''

        return -1




        specialRoads = [[a, b, c, d, x] for a, b, c, d, x in specialRoads if x < abs(a - c) + abs(b - d)]
        dist = {(start[0], start[1]): 0}
        heap = [(0, start[0], start[1])]
        while len(heap) > 0:
            currdist, x, y = heapq.heappop(heap)
            for a, b, c, d, cost in specialRoads:
                if dist.get((c, d), float('inf')) > currdist + abs(x - a) + abs(y - b) + cost:
                    dist[(c, d)] = currdist + abs(x - a) + abs(y - b) + cost
                    heapq.heappush(heap, (dist[(c, d)], c, d))
        res = abs(target[0] - start[0]) + abs(target[1] - start[1])
        for a, b, c, d, cost in specialRoads:
            res = min(res, dist.get((c, d), float('inf')) + abs(target[0] - c) + abs(target[1] - d))
        return res
    

    def dist(x1,x2,y1,y2):
            return abs(x1-x2)+abs(y1-y2)      
  
        self.ans = abs(start[0]-target[0]) + abs(start[1]-target[1])
        hm = dict()

        def helper(curX, curY, curDist):
            # Pruning 1
            if curDist >= self.ans: return
            self.ans = min(self.ans, dist(curX, target[0], curY, target[1]) + curDist)
            
            # Pruning 2
            if (curX, curY) in hm:
                if hm[(curX,curY)] <= curDist:
                    return
            hm[(curX,curY)] = curDist
            
            for next in specialRoads:
                helper(next[2], next[3], curDist + dist(curX, next[0], curY, next[1]) + next[4])

        helper(start[0], start[1], 0)

        return self.ans



    filteredRoads = []
    for road in specialRoads:
        a, b, c, d, cost = road
        if cost < abs(a - c) + abs(b - d):
            filteredRoads.append([a, b, c, d, cost])
    dist = {(start[0], start[1]): 0}
    heap = [(0, start[0], start[1])]
    while heap:
        currdist, x, y = heapq.heappop(heap)
        for road in filteredRoads:
            a, b, c, d, cost = road
            if dist.get((c, d), float('inf')) > currdist + abs(x - a) + abs(y - b) + cost:
                dist[(c, d)] = currdist + abs(x - a) + abs(y - b) + cost
                heapq.heappush(heap, (dist[(c, d)], c, d))
    res = abs(target[0] - start[0]) + abs(target[1] - start[1])
    for road in filteredRoads:
        a, b, c, d, cost = road
        res = min(res, dist.get((c, d), float('inf')) + abs(target[0] - c) + abs(target[1] - d))
    return res