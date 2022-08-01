class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        edge = {}
        #inedge = defaultdict(int)
        
        #for i,e in enumerate(edges):

            #if edges[i] != -1:
                #edge[i] = edges[i]
                #inedge[edges[i]] += 1
        
        h = Deque()

        
        h.append((node1,0))
        h.append((node2,1))

        #print(h)

        v0 = set()
        #v0.add(node1)
        v1 = set()
        #v1.add(node2)
        
        #print(v0)
        #print(v1)
        
        #res = #[float("inf")] * len(edges) 
        
        dist = 0
        
        
        
        while h:
            #print(len(h))
            res = []
            for _ in range(len(h)):
                #print(h)
                ##print(v0)
                #print(v1)
                c, ori = h.popleft()
                #print(c,ori)

                
                if ori == 0:
                    v0.add(c)
                    if edges[c]!=-1 and edges[c] not in v0:
                         h.append((edges[c],ori))
                elif ori == 1:
                    v1.add(c)
                    if edges[c]!=-1 and edges[c] not in v1:
                         h.append((edges[c],ori))
                
                if c in v1 and c in v0:
                    res.append(c)
                
                #print(res)
                
            if len(res) > 0:
                
                return min(res) 

        return -1
            
        
        
        

        
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        

        q = Deque()

        
        q.append((node1,0))
        q.append((node2,1))

        v0 = set()
        v1 = set()

        dist = 0

        
        while q:
            res = []
            
            for _ in range(len(h)):

                node, source = q.popleft()
                
                if source == 0:
                    v0.add(node)
                    if edges[node]!=-1 and edges[node] not in v0:
                         q.append((edges[node],source))
                elif source == 1:
                    v1.add(node)
                    if edges[node]!=-1 and edges[node] not in v1:
                         q.append((edges[node],source))
                
                if node in v1 and node in v0:
                    res.append(node)

            if len(res) > 0:
                return min(res) 

        return -1
            
        
        
        
        