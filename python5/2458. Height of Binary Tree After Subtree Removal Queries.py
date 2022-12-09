# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        
        res = []
        
        d = defaultdict(TreeNode)
        cc = defaultdict(TreeNode)

        hh = []
        
        def dfs(node,s,prev):
            if not node:
                return
            
            d[node.val] = prev
            cc[node.val] = node

            s.add(node.val)

            dfs(node.left,s,node)
            dfs(node.right,s,node)

            if not node.left and not node.right:
                c = s.copy()
                heappush(hh, [ -(len(c)-1), c])

            s.remove(node.val)

        dfs(root, set(), None)
            
        #print(h)
        @cache
        def get(q):
            #print(q)
            h = copy.deepcopy(hh)

            #print(h)
            while h and q in h[0][1]:
                r, se = heappop(h)
                
                cur = cc[q]
                se.remove(q)
                
                while cur :
                    if cur.left and cur.left.val in se:
                        se.remove(cur.left.val)
                        cur = cur.left
                    elif cur.right and cur.right.val in se:
                        se.remove(cur.right.val)
                        cur = cur.right
                    else:
                        cur = None

                heappush(h, [ -(len(se)-1), se])

            if h:
                return -h[0][0]
            else:
                return -1

        return [get(q) for q in queries ]


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        node_to_parent = {}
        value_to_node = {}
        node_to_level = {}
        node_to_depths = {}
        
        def dfs(i, p, d):
            if not i:
                return 0
            value_to_node[i.val] = i
            node_to_parent[i] = p
            node_to_level[i] = d
            l = dfs(i.left, i, d+1)
            r = dfs(i.right, i, d+1)
            node_to_depths[i] = [l, r]
            return max(l, r)+1
        
        dfs(root, None, 0)

        @cache
        def get(q):
            i = value_to_node[q]
            if i == root:
                return -1
            p = node_to_parent[i]
            if p.left == i:
                mx = node_to_level[p] + node_to_depths[p][1]
            else:
                mx = node_to_level[p] + node_to_depths[p][0]
            return max(mx, get(p.val))
        
        return [get(q) for q in queries]   