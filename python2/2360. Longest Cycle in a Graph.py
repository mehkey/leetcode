class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        v = set()
        
        res = -1
        
        for n in range(len(edges)):

            j = 0
            
            prev = {}
            
            while n != -1 and n not in v:
                prev[n] = j
                j+=1
                v.add(n)
                n = edges[n]
            
            if n != -1 and n in prev:
                res = max(res, j - prev[n])
        
        return res




class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        n = len(edges)
        edge = {}
        inedge = defaultdict(int)
        
        total = 0
        
        for i,e in enumerate(edges):

            if edges[i] != -1:
                edge[i] = edges[i]
                inedge[edges[i]] += 1
        
        h = Deque()

        for i in range(n):
            if inedge[i] <= 0:
                h.append((i,0))

        #print(h)
        
        v = set()
        
        m = float('-inf')
        
        while h:
            
            for _ in range(len(h)):
                
                c, ori = h.popleft()
                #print(c,ori)
                if c not in v:
                    v.add(c)
                
                if edges[c] != -1 and edges[c] not in v:
                    h.append((edges[c],ori+1))
                
                if edges[c] in v:
                    m = max(m, ori+1)

            if len(v) == n:
                break 
            else:
                for i in range(n):
                    if i not in v:
                        h.append((i,0))
            
        return -1 if m == float('-inf') else m