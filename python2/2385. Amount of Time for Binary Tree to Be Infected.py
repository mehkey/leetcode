# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        tree = defaultdict(set)
        
        def dfs(n,prev):
            if not n:
                return
            
            if prev != None:
                tree[n.val].add(prev)
                tree[prev].add(n.val)
            
            if n.right:
                tree[n.val].add(n.right.val)
                tree[n.right.val].add(n.val)

            if n.left:
                tree[n.val].add(n.left.val)
                tree[n.left.val].add(n.val)
            
            dfs(n.left,n.val)
            dfs(n.right,n.val)
        
        dfs(root,None)
        
        q = deque()
        q.append(start)
        
        level = 0
        visited = set([start])
        
        while q:

            for i in range(len(q)):
                v = q.popleft()

                for c in tree[v]:
                    if c not in visited:
                        q.append(c)
                        visited.add(c)
            level+=1
                
        return level -1
        
        """
        self.depth = 0
        
        def dfs(n):
            
            if not n:
                return 0
            
            return max(dfs(n.left)+1, dfs(n.right)+1)

        
        def find(n,l):
            
            if not n:
                return False
            
            if n.val == start:
                self.v = l+1

            return find(n.left,l+1) or  find(n.right,l+1)

        d = dfs(root)
        
        f = find(root,0)

        if root.val == start:
            #print(d)
            return d - 1
        
        self.v = -1
        self.c = None
        
        find(root.left,0)
        l = self.v

        self.v = -1
        find(root.right,0)
        r = self.v

        #print(d)
        #print(l)
        #print(r)
        
        if l != -1:
            return max( dfs(root.right) -1 + 1 + l, d - 1 - l  )
        if r != -1:
            return max( dfs(root.left) -1 + 1 + r, d - 1 - r  )
        """
