# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        q = deque()

        q.append(root)

        res= []
        z = True

        
        while q:
            l = len(q)
            lev = []
            for _ in range(l):

                cur = q.popleft()
                lev.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if z:
                res.append(lev)
            else:
                res.append(lev[::-1])
            z = not z

        #print(res)
        return res



