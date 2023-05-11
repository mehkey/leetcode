class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        
        
        max_p = 0
        
        v = [0] * n
        
        def dfs(node,s):
            nonlocal max_p
            if node > n:
                max_p= max(max_p,s)
                return s
            
            l = dfs(node*2,s+cost[node-1])
            r = dfs(node*2+1,s+cost[node-1])
            
            v[node-1] = max(l,r)

            return max(l,r)
        
        total = 0
        
        def dfs2(node,extra):
            nonlocal total
            nonlocal max_p
            
            if node > n:
                return #s

            diff= max_p - v[node-1] - extra
            
            total += diff
            
            left = dfs2(node*2,extra + diff)
            
            right = dfs2(node*2+1,extra + diff)
            
            #total += max(left,right) - max_p
            
            #return max(left,right)
        
        dfs(1,0)
        
        #print(v)
        
        dfs2(1,0)

        return total