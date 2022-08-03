# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        edges = defaultdict(list)
        indeg =  defaultdict(int)
        for p,c,isLeft in descriptions:
            edges[p].append((c,isLeft))
            indeg[c] += 1
        
        #print(edges)
        root = 0
        s = set(map(lambda x: x[0], descriptions)) | set(map(lambda x: x[1], descriptions)) 
        #print(s)
        for c in s:
            print(c)
            if indeg[c] == 0:
                root = c
                break
        
        #print(root)
        
        def dfs(root):
            if root == -1:
                return None
            
            t = TreeNode(root)
            
            for e in edges[root]:
                if e[1] == 1:
                    t.left = dfs(e[0])
                if e[1] == 0:
                    t.right = dfs(e[0])
            
            return t
        
        return dfs(root)
        
        