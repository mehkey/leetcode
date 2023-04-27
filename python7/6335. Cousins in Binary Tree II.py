# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        '''
        def dfs(node1,node2,parent1,parent2):
            
            #print(node1,node2)
            if not node1 :
                return None
            
            n_node = TreeNode()
            
            n2r = node2.right if node2 else None
            n2l = node2.left if node2 else None
            
            left = dfs(node1.left,n2r, node1,node2)
            right = dfs(node1.right,n2l, node1,node2)

            if left:
                n_node.left = left
            if right:
                n_node.right = right
            
            if node1 != node2 and parent1 != parent2 :
                #if node2 == parent2.left:
                    #n_node.val = 
                #n_node.val = node2.val + parent2
                if parent2:
                    #print(parent2.val)
                    n_node.val = (parent2.left.val if parent2.left else 0) + (parent2.right.val if parent2.right else 0)
                
            return n_node
        

        return dfs(root,root,None,None)
        '''
        G = defaultdict(int)
        def dfs1(node1,level):
            
            if not node1 :
                return None

            if level >= 1:
                G[level] += node1.val

            left = dfs1(node1.left,level+1)
            right = dfs1(node1.right,level+1)


        def dfs2(node1,parent,level):

            if not node1 :
                return None
            
            n_node = TreeNode()

            if parent:

                n_node.val = G[level] -  (parent.left.val if parent.left else 0) - (parent.right.val if parent.right else 0)

            n_node.left = dfs2(node1.left,node1,level+1)
            n_node.right = dfs2(node1.right,node1,level+1)

            return n_node

        dfs1(root,0)

        return dfs2(root,None,0)
        
