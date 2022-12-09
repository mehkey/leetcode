# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:

        '''
        deff = []

        def binary_search(arr, x, left):
            low = 0
            high = len(arr) - 1
            mid = 0

            while low <= high:

                mid = (high + low) // 2

                if arr[mid] < x:
                    low = mid + 1

                elif arr[mid] > x:
                    high = mid - 1

                else:
                    return mid
            
            if left and mid == 0:
                return -1
            
            if left:
                return low
            
            if not left and mid == len(arr) -1:
                return -1
            
            return high
        
        def dfs(node):

            if not node:
                return     

            dfs(node.left)
            deff.append(node.val)
            dfs(node.right)

        dfs(root)

        res = []
        #print(deff)
        for query in queries:
            #print(query)
            #a = bisect_left(deff,query)
            #a = binary_search(deff,query)
            
            a = binary_search(deff,query,True)
            
            b = binary_search(deff,query,False)

            #if deff[a] == query:
                #res
            #    left = q

            #if deff[b] == query:
            #    query = 1

            res.append([deff[a] if a != -1 else -1, deff[b] if b != -1 else -1])
            

            #bisect_left(deff,query)
            
        return res
        
        '''
        
        def dfs(root, arr):
            if not root: return
            dfs(root.left, arr)
            arr.append(root.val)
            dfs(root.right, arr)
        arr = []
        dfs(root, arr)
        ans = []
        n = len(arr)
        for key in queries:
            left, right = 0, n - 1
            while right >= left:
                mid = (right + left) // 2
                if arr[mid] == key:
                    break
                elif arr[mid] > key:
                    right = mid - 1
                else:
                    left = mid + 1
            if arr[mid] == key:
                ans.append([arr[mid], arr[mid]])
            elif arr[mid] > key:
                if (mid - 1) >= 0:
                    ans.append([arr[mid - 1], arr[mid]])
                else:
                    ans.append([-1, arr[mid]])
            else:
                if (mid + 1) < n:
                    ans.append([arr[mid], arr[mid + 1]])
                else:
                    ans.append([arr[mid], -1])
        return ans
