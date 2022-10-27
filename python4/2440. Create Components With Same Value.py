class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:

        
        '''
        def dfs(u: int) -> int:
     

            self.visit[u] = True
            currComponentNode = 0

            for i in range(len(self.g[u])):
                v = self.g[u][i]

                if (not self.visit[v]):

                    subtreeNodeCount = dfs(v)
                    
                    if subtreeNodeCount == -1:
                        return -1

                    if (subtreeNodeCount == self.count):
                        self.res += 1
                        #currComponentNode = 0

                    else:
                        currComponentNode += subtreeNodeCount  % self.count
                        


            currComponentNode += nums[u]
            
            #if currComponentNode > self.count:
                #return -1
            
            return currComponentNode % self.count
            


        def maxEdgeRemovalToMakeForest(N: int) -> int:


            self.visit = [False for _ in range(N + 1)]
            
            self.res = 0
            
            d = dfs(0)
            
            if d == -1:
                return 0
                #return self.res
            
            #if d == self.count:
                #return self.res
            
            if d != self.count :
                return 0

            return self.res

        def addEdge(u: int, v: int) -> None:


            self.g[u].append(v)
            self.g[v].append(u)
 
        res = 0

        N = len(nums)
        E = len(edges)
        

        r = 0
        for i in range(1, sum(nums)//N +1 ):
            
            
            self.count = i
            self.g = [[] for _ in range(N)]
            
            for j in range(E):
                
                addEdge(edges[j][0], edges[j][1])
            
            c = maxEdgeRemovalToMakeForest(N)
            r = max( r,  c )
            

        return r
        
        
        
        
        tree=collections.defaultdict(set)
        for i,j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def check(cur,prev,target):
            val=nums[cur]
            for kid in tree[cur]-{prev}:
                i=check(kid,cur,target)
                if i==-1: return -1
                val+=i          
            return val%target if val<=target else -1

        tot=sum(nums)
        for n in range(min(tot//max(nums),len(nums)),0,-1):  # for simplicity, i do not use O(n^1/2) approach to find all factors here
            if not tot%n and check(0,-1,tot//n)==0:
                return n-1
                
        '''
        
        n = len(nums)
        t = sum(nums)
        G = defaultdict(list)
        self.components = 0
        for v, w in edges:
            G[v].append(w)
            G[w].append(v)
        def dfs(v, t, visited):
            if v in visited: return 0
            visited.add(v)
            res = nums[v]
            for w in G[v]:
                res += dfs(w, t, visited)
            if res == t:
                self.components += 1
            return res if res != t else 0
        
        a = 0
        for i in range(2, n+1):
            if t % i == 0:
                #print(i, t, n)
                self.components = 0
                dfs(0, t//i, set())
                if self.components == i:
                    a= max(a, i - 1)
        return a