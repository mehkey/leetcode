class segtree():
    def __init__(self, n, nums):
        self.lazy = defaultdict(int)
        self.len = defaultdict(int)
        self.tree = defaultdict(int)
        # initial length and summation
        self.init_len(1, 0, n, 0, n, nums)
        self.init_num(1, 0, n, 0, n, nums)
        
    def init_len(self, ind, ul, ur, cl, cr, num):
        if cr < cl or cl >= len(num):
            return 0
        if cr == cl:
            self.len[ind] = 1
            return 1
        mid = (cl + cr) // 2
        if cl != cr:
            self.init_len(ind*2, ul, ur, cl, mid, num)
        self.init_len(ind*2+1, ul, ur, mid+1, cr, num)
        self.len[ind] = self.len[ind*2] + self.len[ind*2+1]
    
    def init_num(self, ind, ul, ur, cl, cr, num):
        if cr < cl or cl >= len(num):
            return
        if cl == cr:
            self.tree[ind] = num[cl]
            return
        mid = (cl + cr) // 2
        if cl != cr:
            self.init_num(ind*2, ul, ur, cl, mid, num)
        self.init_num(ind*2+1, ul, ur, mid+1, cr, num)
        
        self.tree[ind] = self.tree[ind*2] + self.tree[ind*2+1]
        
    
    def proplazy(self, ind):
        # if the parent node has the notation to flip, then we update all summation of children nodes.
        if self.lazy[ind]:
            self.lazy[ind*2] ^= self.lazy[ind]
            self.tree[ind*2] = self.len[ind*2] - self.tree[ind*2]
            self.lazy[ind*2 + 1] ^= self.lazy[ind]
            self.tree[ind*2 + 1] = self.len[ind*2+1] - self.tree[ind*2 + 1]
            self.tree[ind] = self.tree[ind*2] + self.tree[ind*2+1]
            self.lazy[ind] = 0
        
    def update(self, ind, ul, ur, cl, cr):
        if cl > ur or cr < ul:
            return 
        if ul <= cl and cr <= ur:
            # mark to flip
            self.lazy[ind] ^= 1
            self.tree[ind] = self.len[ind] - self.tree[ind]
        else:
            mid = (cl + cr) // 2
            self.proplazy(ind)
            self.update(ind*2, ul, ur, cl, mid)
            self.update(ind*2+1, ul, ur, mid+1, cr)
            self.tree[ind] = self.tree[ind*2] + self.tree[ind*2+1]
           
    def query(self, ind, ul, ur, cl, cr):
        if cl > ur or cr < ul:
            return 0
        if ul <= cl and cr <= ur:
            return self.tree[ind]
        else:
            mid = (cl + cr) // 2
            self.proplazy(ind)
            return self.query(ind*2, ul, ur, cl, mid) + self.query(ind*2+1, ul, ur, mid+1, cr)
         
class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        seg = segtree(len(nums1) + 10, nums1)
        anss = []
        ans = sum(nums2)
        n = len(nums1) + 10
        for i, j, k in queries:
            if i == 1:
                seg.update(1, j, k, 0, n)
            if i == 2:
                ans += seg.tree[1] * j
            if i == 3:
                anss.append(ans)
        return anss

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        l = len(nums1)
        init = 1<<l
        nums1 = int("".join(map(str, nums1)), 2)
        cur= sum(nums2)
        ans =[]
        for f,s,t in queries:
            if f==1:
                a = (init>>s)-1
                b = (init>>(t+1))-1
                nums1 = nums1^a^b
            elif f==2:
                cnt =nums1.bit_count()
                cur+=s*cnt
            else:
                ans.append(cur)
        return ans
                
            