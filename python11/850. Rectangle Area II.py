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

'''
class LazySegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the lazy segment tree with data"""
        self._default = default
        self._func = func

        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self._lazy = [0] * (2 * _size)

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __len__(self):
        return self._len

    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        q, self._lazy[idx] = self._lazy[idx], 0

        self._lazy[2 * idx] += q
        self._lazy[2 * idx + 1] += q
        self.data[2 * idx] += q
        self.data[2 * idx + 1] += q

    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]
            idx >>= 1

    def add(self, start, stop, value):
        """lazily add value to [start, stop)"""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazy[start] += value
                self.data[start] += value
                start += 1
            if stop & 1:
                stop -= 1
                self._lazy[stop] += value
                self.data[stop] += value
            start >>= 1
            stop >>= 1

        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)

    def query(self, start, stop, default=0):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        # Apply all the lazily stored queries
        self._update(start)
        self._update(stop - 1)

        res = default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "LazySegmentTree({0})".format(self.data)

'''

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        
        '''
        #rectangles.sort(key = lambda x: (x[0],x[2])
        MOD = 10**9 + 7

        events1 = [ (y0,x0,x1,1) for x0,y0,x1,y1 in rectangles]

        events2 = [ (y1,x0,x1,-1) for x0,y0,x1,y1 in rectangles]


        allE = sorted(events1+events2)

        st = SegmentTree()

        for y, x0,x1, diff in allE:

            area += (y - y0) * cur_x

            for i in range(x0,x1):


        return area % MOD

        


        ev = defaultdict(list)
        for a, b, c, d in rectangles:
            ev[a].append((b, 1))
            ev[a].append((d, -1))
            ev[c].append((b, -1))
            ev[c].append((d, 1))
        seg = {}
        prv = 0
        width = 0
        ret = 0
        for k in sorted(ev.keys()):
            ret += width * (k - prv)
            for x, d in ev[k]:
                seg[x] = seg.get(x, 0) + d
                if seg[x] == 0:
                    del seg[x]
            width = 0
            st = 0
            left = None
            for x in sorted(seg.keys()):
                st += seg[x]
                if st > 0 and left is None:
                    left = x
                if st == 0 and left is not None:
                    width += x - left
                    left = None
            prv = k
        return ret % (10**9+7)

        '''

        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        ys = sorted(set([y for x1, y1, x2, y2 in rectangles for y in [y1, y2]]))
        x_i = {v: i for i, v in enumerate(xs)}
        y_i = {v: i for i, v in enumerate(ys)}
        m, n = len(y_i), len(x_i)
        
        grid = [[0] * m for _ in range(n)]
        for x1, y1, x2, y2 in rectangles:
            for x in range(x_i[x1], x_i[x2]):
                for y in range(y_i[y1], y_i[y2]):
                    grid[x][y] = 1

        ans = 0
        for x in range(n-1):
            for y in range(m-1):
                ans += grid[x][y]*(xs[x+1] - xs[x]) * (ys[y+1] - ys[y])
        return ans  % (10**9 + 7)

        N = len(rectangles)

        events = defaultdict(list)

        xs = set()

        for x0,y0,x1,y1 in rectangles:

            events[y0].append((1,x0,x1))
            events[y1].append((-1,x0,x1))

            xs.add(x0)
            xs.add(x1)

        xss = sorted(xs)
        xsi = {xi: i for i,xi in enumerate(xss)}

        #events.sort()

        prevy = 0

        count = defaultdict(int)

        a , xsum , prevy= 0,0,0

        for y in sorted(events):

            a += (y-prevy) * xsum

            for change, x0, x1 in events[y]:
                for i in range(xsi[x0],xsi[x1]):
                    count[i] += change

            prevy = y

            xsum = 0

            for i in range(len(xss)-1):
                xsum += (xss[i+1] - xss[i]) * (1 if count[i] > 0 else 0)

        return a % (10**9+7)



        N = len(rectangles)

        events = []

        xs = set()

        for x0,y0,x1,y1 in rectangles:

            events.append((y0,1,x0,x1))
            events.append((y1,-1,x0,x1))

            xs.add(x0)
            xs.add(x1)

        xss = sorted(xs)
        xsi = {xi: i for i,xi in enumerate(xss)}

        events.sort()

        prevy = 0

        count = defaultdict(int)

        a , xsum , prevy= 0,0,0

        for y, change, x0, x1 in events:

            a += (y-prevy) * xsum

            prevy = y

            for i in range(xsi[x0],xsi[x1]):
                count[i] += change

            xsum = 0

            for i in range(len(xss)-1):
                xsum += (xss[i+1] - xss[i]) * (1 if count[i] > 0 else 0)

        return a % (10**9+7)





        #index i means the interval from xs[i] to xs[i+1]
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))

        xs_i = {x:i for i, x in enumerate(xs)}

        #print(xs)
        #print(xs_i)
        data = [0 for x in xs]
        st = SegmentTree(data)

        L = []
        for x1, y1, x2, y2 in rectangles:
            L.append([y1, 1, x1, x2])
            L.append([y2, -1, x1, x2])
        L.sort()
        cur_y = cur_x_sum = area = 0
        #print(L)
        for y, open_close, x1, x2 in L:
            print(y,cur_y, cur_x_sum)
            area += (y - cur_y) * cur_x_sum
            cur_y = y
            #one index corresponds to one interval, that's why we use xs_i[x2]-1 instead of xs_i[x2]
            #st.update(1, 0,  len(xs) - 1, xs_i[x1], xs_i[x2]-1, open_close)
            for i in range(xs_i[x1],xs_i[x2]):
                #st[]
                st[i] = st[i] + open_close

            #print(st)
            cur_x_sum = st.query(0, len(xs)) #st.data[0] #st.query(0, len(xs)-1) 
            
        return area % (10 ** 9 + 7)
