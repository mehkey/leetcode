
class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1

        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)

class Solution:
    def leftmostBuildingQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:

        que = [[] for a in A]
        h = []
        res = [-1] * len(queries)
        for qi, (i, j) in enumerate(queries):
            if (i <  j) == ( A[i] < A[j]):
                res[qi] = max(i, j)
            else:
                que[max(i, j)].append([max(A[i], A[j]), qi])
        print(que)
        #print(res)
        #print(h)
        for i, a in enumerate(A):
            print(h)
            while h and h[0][0] < a:
                res[heappop(h)[1]] = i
            for q in que[i]:
                heappush(h, q)
            print(res)
        return res
        
        N = len(heights)

        s = SegmentTree(heights)

        res = [-1] * len(queries)

        for qi, (A, B) in enumerate(queries):
            
            if A > B:
                A,B = B,A

            mm = max(heights[A],heights[B])

            l = max(A,B) + 1
            r = N -1
            
            q = s.query(l,r+1)
            
            if A == B:
                res[qi] = B
                continue
            
            if heights[A] < heights[B]:
                res[qi] = B
                continue

            if q <= mm :
                res[qi] = -1
                continue

            qq = max(A,B) + 1
            
            # 0. 4
            # 1 1 2 3 8

            while l <= r:
                
                mid = (l+r)//2

                q = s.query(l,mid+1)
                
                if q > mm:
                    r = mid - 1
                else:
                    
                    l = mid + 1
                    qq = max(qq,l)

            res[qi] = l

        return res

        
        
        n = len(heights)
        st = SegmentTree(heights)
        
        ret = []
        for a, b in queries:
            if a == b:
                ret.append(b)
                continue
            if a < b and heights[a] < heights[b]:
                ret.append(b)
                continue
            if b < a and heights[b] < heights[a]:
                ret.append(a)
                continue
            v = max(heights[a], heights[b]) + 1
            l, r = max(a, b) + 1, n-1
            if l >= n or st.query(l, n) < v:
                ret.append(-1)
                continue
                
            mm = 0
            
            while l <= r:
                mi = (l+r)//2
                
                res = st.query(l, mi+1)
                
                if res >= v:
                    
                    mm = max(mm, l)
                    r = mi 
                else:
                    #mm = max(mm, l)
                    l = mi + 1
            ret.append(mm)
        return ret

'''class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        
        arr = []
        
        cur = []
        n = len(heights)
        for h in heights:
            
            cur.append((h,i))
            
            while len(cur) > 1 and cur[-1] < cur[-2]:
                cur.pop()

            i++
        
        i = 0
        for h in heights:
            
            while cur and cur[0][1] < i:
                cur.popleft()
            
            if not cur:
                for j in range(i+1,n):
                    cur.append((h,j))
            
                    while len(cur) > 1 and cur[-1] < cur[-2]:
                        cur.pop()

            arr[i] = cur[:]
            
            i++
        
        res = []
        for a,b in queries:
            
            l = 0
            r = 0
            while l < len(arr[a]) and r < len(arr[b]):

                #if arr[a] == arr[b]:
                #    res.append()
                #l += 1
                #r += 1

            res.append()
'''