# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        G = defaultdict(list)

        def add(node1,node2):
            G[node1].append(node2)
            G[node2].append(node1)

        def dfs(node):
            if not node:
                return 
            
            m = 0
            if node.left:
                add(node.val, node.left.val)
                dfs(node.left)
            
            if node.right:
                add(node.val, node.right.val)
                dfs(node.right)
        dfs(root)
        q = deque()
        q.append(start)
        vis = set()
        steps = -1
        while q:
            steps += 1
            ql = len(q)
            for _ in range(ql):
                cur = q.popleft()
                if cur not in vis:
                    vis.add(cur)
                for n in G[cur]:
                    if n not in vis:
                        q.append(n)
        
        return steps