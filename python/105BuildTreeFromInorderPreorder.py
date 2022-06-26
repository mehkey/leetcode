# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        """
        
          2
          
        1   3
        
        
        preorder 213
        
        inorder 123
        
        
        tree
        
          2
          
        1   3
        
        Start at the parent
        create a node
        
        find all the elements in the left
        find all elements in the right
        create a new node where preorder tells you the parent on the left and right
        """
        
        if len(preorder) == 0 or len(inorder) ==0:
            return None
        
        """
        def buildTree(preorder,inorder, node):
            
            if len(preorder) == 0 or len(inorder) == 0:
                return None
            
            node.val = preorder[0]
            
            left = TreeNode()
            right = TreeNode()

            node.left = left
            node.right = right

            buildTree(preorder[1:],inorder[0:inorder.index(node.val)])
            buildTree(preorder[2:],inorder[inorder.index(node.val)+1:])

        buildTree(preorder,inorder,node)

        return node"""

        def buildTree(preorder,inorder):

            #print('hi')
            if len(preorder) == 0 or len(inorder) == 0:
                return None

            node = TreeNode(preorder[0])

            mid = inorder.index(node.val)

            node.left =  buildTree(preorder[1:mid+1],inorder[0:mid])
            node.right = buildTree(preorder[mid+1:],inorder[mid+1:])

            return node

        #print('HI')
        return buildTree(preorder,inorder)

    
    runtime O(n + m) O(n)
    space (n)
        
        
        
        
        
        