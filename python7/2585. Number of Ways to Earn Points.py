

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        stack = [(root, 0)]
        while stack: 
            node, i = stack.pop()
            if i == len(vals): vals.append(0)
            vals[i] += node.val 
            if node.left: stack.append((node.left, i+1))
            if node.right: stack.append((node.right, i+1))
        return sorted(vals, reverse=True)[k-1] if len(vals) >= k else -1