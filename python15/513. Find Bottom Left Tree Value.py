# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root):
        result = [0, 0]
        self.help(root, 1, result)
        return result[1]

    def help(self, node, currD, result):
        if node is None:
            return

        # If we have reached a new level
        if currD > result[0]:
            result[0] = currD
            result[1] = node.val

        # Explore left and right subtrees
        self.help(node.left, currD + 1, result)
        self.help(node.right, currD + 1, result)