class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        gr = defaultdict(set)
        gc = defaultdict(set)
        
        for row in rowConditions:
            gr[row[0]].add(row[1])

        for col in colConditions:
            gc[col[0]].add(col[1])
        
        orr = list()
        occ = list()
        vr = defaultdict(bool)
        vc = defaultdict(bool)
        
        def dfs(i,v,o,g):
            if i in v:
                return v[i]

            v[i] = True
            for n in g[i]:
                if dfs(n,v,o,g):
                    return True
            v[i] = False
    
            o.append(i)

        for i in range(1,k+1):
            if dfs(i,vr, orr,gr):
                return []

        for i in range(1,k+1):
            if dfs(i,vc, occ,gc):
                return []

        orr.reverse()
        occ.reverse()

        res = [[0 for i in range(k)] for j in range(k)]

        pos = [[0,0] for i in range(k+1)]
        for i,v in enumerate(orr):
            pos[v][0] = i
        for i,v in enumerate(occ):
            pos[v][1] = i
        
        for i,p in enumerate(pos):
            if i == 0:
                continue
            res[p[0]][p[1]] = i

        return res
    
    
    
        graph_row = defaultdict(set)
        graph_col = defaultdict(set)
        
        for row in rowConditions:
            graph_row[row[0]].add(row[1])

        for col in colConditions:
            graph_col[col[0]].add(col[1])
        
        order_row = list()
        order_col = list()
        visited_row = defaultdict(bool)
        visited_col = defaultdict(bool)
        
        def dfs(i,v,o,g):
            if i in v:
                return v[i]

            v[i] = True
            for n in g[i]:
                if dfs(n,v,o,g):
                    return True
            v[i] = False
    
            o.append(i)

        for i in range(1,k+1):
            if dfs(i,visited_row, order_row,graph_row):
                return []

        for i in range(1,k+1):
            if dfs(i,visited_col,order_col ,graph_col):
                return []

        order_row.reverse()
        order_col.reverse()
        
        pos = [[0,0] for i in range(k+1)]

        for i,v in enumerate(order_row):
            pos[v][0] = i
        for i,v in enumerate(order_col):
            pos[v][1] = i
        
        res = [[0 for i in range(k)] for j in range(k)]

        for i,p in enumerate(pos):
            if i == 0:
                continue
            res[p[0]][p[1]] = i

        return res



class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        gr = defaultdict(set)
        gc = defaultdict(set)
        
        inr = defaultdict(int)
        inc = defaultdict(int)
        
        for row in rowConditions:
            gr[row[0]].add(row[1])
            inr[row[1]]+=1

        for col in colConditions:
            gc[col[0]].add(col[1])
            inc[col[1]]+=1
        
        qr = deque()
        qc = deque()
        
        for g in range(1,k+1):
            if inr[g] == 0:
                qr.append(g)

        for g in range(1,k+1):
            if inc[g] == 0:
                qc.append(g)
        
        orr = list()
        occ = list()
        
        #print(inr)
        #print(inc)
        seen= set()
        while qr:

            cur = qr.popleft()
            seen.add(cur)
            orr.append(cur)
            
            
            for n in gr[cur]:
                inr[n] -= 1
                if inr[n] == 0:
                    qr.append(n)
        if len(seen) != k:
            return []
        seen = set()
        while qc:

            cur = qc.popleft()
            
            occ.append(cur)
            seen.add(cur)
            for n in gc[cur]:
                inc[n] -= 1
                if inc[n] == 0:
                    qc.append(n)
        
        if len(seen) != k:
            return []
        
        res = [[0 for i in range(k)] for j in range(k)]

        pos = [[0,0] for i in range(k+1)]
        for i,v in enumerate(orr):
            pos[v][0] = i
        for i,v in enumerate(occ):
            pos[v][1] = i
        
        for i,p in enumerate(pos):
            if i == 0:
                continue
            res[p[0]][p[1]] = i

        return res
    

            
        
        """
        gr = defaultdict(set)
        gc = defaultdict(set)
        
        for row in rowConditions:
            gr[row[0]].add(row[1])

        for col in colConditions:
            gc[col[0]].add(col[1])
        
        orr = list()
        occ = list()
        vr = defaultdict(bool)
        vc = defaultdict(bool)
        
        def dfs(i,v,o,g):
            if i in v:
                return v[i]

            v[i] = True
            for n in g[i]:
                if dfs(n,v,o,g):
                    return True
            v[i] = False
    
            o.append(i)

        for i in range(1,k+1):
            if dfs(i,vr, orr,gr):
                return []

        for i in range(1,k+1):
            if dfs(i,vc, occ,gc):
                return []

        orr.reverse()
        occ.reverse()

        res = [[0 for i in range(k)] for j in range(k)]

        pos = [[0,0] for i in range(k+1)]
        for i,v in enumerate(orr):
            pos[v][0] = i
        for i,v in enumerate(occ):
            pos[v][1] = i
        
        for i,p in enumerate(pos):
            if i == 0:
                continue
            res[p[0]][p[1]] = i

        return res
    
    
    
        graph_row = defaultdict(set)
        graph_col = defaultdict(set)
        
        for row in rowConditions:
            graph_row[row[0]].add(row[1])

        for col in colConditions:
            graph_col[col[0]].add(col[1])
        
        order_row = list()
        order_col = list()
        visited_row = defaultdict(bool)
        visited_col = defaultdict(bool)
        
        def dfs(i,v,o,g):
            if i in v:
                return v[i]

            v[i] = True
            for n in g[i]:
                if dfs(n,v,o,g):
                    return True
            v[i] = False
    
            o.append(i)

        for i in range(1,k+1):
            if dfs(i,visited_row, order_row,graph_row):
                return []

        for i in range(1,k+1):
            if dfs(i,visited_col,order_col ,graph_col):
                return []

        order_row.reverse()
        order_col.reverse()
        
        pos = [[0,0] for i in range(k+1)]

        for i,v in enumerate(order_row):
            pos[v][0] = i
        for i,v in enumerate(order_col):
            pos[v][1] = i
        
        res = [[0 for i in range(k)] for j in range(k)]

        for i,p in enumerate(pos):
            if i == 0:
                continue
            res[p[0]][p[1]] = i

        return res
        """
