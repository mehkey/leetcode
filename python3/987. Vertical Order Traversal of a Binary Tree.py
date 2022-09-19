# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        """
        
        Approaches: O (n log n + n )
        
        1. DFS to save the position and node into list. Sort the the list at the end and returned a compressed version
        
        O (n log n + n )

        2. BFS (queue) either works
        
        
        Store directly into a ordereddict() # key = x values is [level, number]
        
        
        
        
        
        
        """
        self.nodes = []
        
        
        
        def dfs(node, level, x):
            
            if not node:
                return
            
            dfs(node.left, level+1, x-1)
            
            self.nodes.append((node.val, level,x))
            
            dfs(node.right, level+1, x+1)
        
        
        dfs(root, 0, 0)
        
        #print(self.nodes)
        self.nodes = sorted(self.nodes, key=lambda x: (x[2], x[1], x[0]))
        #print(self.nodes)
        od = defaultdict(list)
        for x in self.nodes:
            od[x[2]].append(x[0])
        #od = {x[2]: x[0] for x in self.nodes }
        #print(od)
        od = OrderedDict(od)
        
        #self.nodes = { x[]}
        
        return od.values()
    
    # list(itertools.groupby(self.nodes, ))
               
        
        
        
        
        
        
            
            
        