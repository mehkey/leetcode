# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        
        [1,2,3,null,null,4,5]
        
        [1,2,3,N,N,4,N,N,5,N,N]
        
        
                     1
               2           3
           N.     N.    4.    5
                       N. N.  N. N
                       
        
        ROOT ->  RECURSIVE DFS
        
        NODE -> add to list
        DFS on chidren
        
        None -> add 'N'
        
        return ",".join(res)
        
        time:O(n) nodes
        time:O(n) nodes
        
        
        1,2,N,N,3,4,N,N,5,N,N
        """
        res = []
        
        def dfs(node):
            if not node:
                res.append('N')
                return
            
            res.append(str(node.val))
            
            dfs(node.left)
            dfs(node.right)
            
            return
        
        dfs(root)
        #print(",".join(res))
        return ",".join(res)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        
        
 offset. 0 1.2 3 4 5 6 7 8 9 ...       
        [1,2,3,N,N,4,N,N,5,N,N]
        
        
                     1
               2           3
           N.     N.    4.    5
                       N. N.  N. N
        
        
        val = res.split(',')
        offset
        
        ROOT ->  offset id = 0 ... 
        
        DFS()
        
        for each id
           create a  Node
           
           DFS()
           DFS()
        
        return root
        
        time:O(n) nodes
        time:O(n) nodes
        
        """
        val = data.split(',')
        offset = 0
        
        def dfs():
            nonlocal offset
            if val[offset] == 'N':
                offset +=1 
                return None
        
            node = TreeNode(val[offset])
            
            offset +=1 
            
            node.left = dfs() #offest +1 
            node.right = dfs() #offest +1
            
            return node
        
        return dfs()
            
                
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))