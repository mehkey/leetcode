class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        '''
        intervals.sort()

        tup = set()

        for interval in intervals:
            tup.add((interval[0],interval[1]))

        g = 0
        
        while len(tup) > 0:
            
            intervals = sorted(list(tup))
            #print(tup)
            #print(intervals)
            cur = 0

            cur = intervals[0]
            #print(cur)
            tup.remove(cur)
            for i in range(1,len(intervals)):
                if intervals[i][0] > cur[1]:
                    cur = intervals[i]
                    tup.remove(intervals[i])

            g += 1
            
        return g
        

        d = defaultdict(int)

        for start, end in intervals:
            d[start]+= 1
            d[end+1]-= 1


        return max(accumulate([d[n] for n in sorted(d.keys())]))
        .
        

        intervals.sort()
        heap = [intervals.pop(0)[1]]

        for start, end in intervals:
            print(heap)
            if start <= heap[0]:
                heappush(heap, end)

            else:
                heappushpop(heap, end)

        return len(heap)
        '''