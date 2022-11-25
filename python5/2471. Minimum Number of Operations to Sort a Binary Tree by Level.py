# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        
        
        q = Deque()
        
        q.append(root)
        
        res = 0
        
        while q:
            arr = []
            
            for _ in range(len(q)):
                
                node = q.popleft()

                if node.left:
                    arr.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    arr.append(node.right.val)
                    q.append(node.right)
            
            res += minSwap(arr,len(arr))
        
        return res

def minSwap(arr, n):

    ans = 0
    temp = arr.copy()


    h = {}

    temp.sort()

    for i in range(n):

        h[arr[i]] = i

    init = 0

    for i in range(n):

        if (arr[i] != temp[i]):
            ans += 1
            init = arr[i]

            arr[i], arr[h[temp[i]]] = arr[h[temp[i]]], arr[i]

            h[init] = h[temp[i]]
            h[temp[i]] = i

    return ans