class Solution:
    
    

    
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        """
        adj = defaultdict(set)
        
        for e in edges:
            
            adj[e[0]].add(e[1])
            adj[e[1]].add(e[0])
        
        t = 0
        
        r = set()
        
        for i in range(n):
            
            if
                t += n - len(adj[e[i]]) + 1 
        
        
        return t
        """
        class dsu:
            def __init__(self,n):
                self.parent=[i for i in range(n)]
                self.size=[1]*n

            def find(self,x):
                if x!=self.parent[x]:
                    self.parent[x]=self.find(self.parent[x])
                return self.parent[x]
            def union(self,u,v):
                u,v=self.find(u),self.find(v)
                #print(u)
                #print(v)
                if u!=v:
                    if self.size[u]<self.size[v]:
                        u,v=v,u
                    self.size[u]+=self.size[v]
                    self.size[v]=0
                    self.parent[v]=u

            def cout(self):
                mp=defaultdict(int)
                for i in range(n):
                    mp[self.find(i)]+=1
                return mp

        d=dsu(n)

        #print(n)

        for u,v in edges:
            #print(d.parent)
            if d.find(u)!=d.find(v):
                #print("--",d.parent)
                d.union(u,v)

        #print(d.size)
        #print(d.parent)
        mp=d.cout()
        print(mp)
        ans=0
        for i in mp:
            ans+=(mp[i]*(n-mp[i]))
        return ans//2