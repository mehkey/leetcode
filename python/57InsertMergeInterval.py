class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        """
        if len(intervals) == 0:
            return [newInterval]
        
        toMergeL = 0
        toMergeR = 0
        
        foundL = False
        foundR = False
        
        count = 0
        
        for interval in intervals:
            
            if not foundL and newInterval[0] >= interval[0] and newInterval[0] <= interval[1] :
                
                foundL = True
                toMergeL = count
                
            if not foundR and newInterval[1] >= interval[0] and newInterval[1] <= interval[1] :
                foundR = True
                toMergeR = count
            
            count += 1
        
        merged = [float("inf"),float("-inf")]
        #for i in range(toMergeL, toMergeR):
        merged[0] = min(merged[0],intervals[toMergeL][0])
        merged[1] = max(merged[1],intervals[toMergeR][1])
        
        merged[0] = min(merged[0],newInterval[0])
        merged[1] = max(merged[1],newInterval[1])

        

        res = []
        if toMergeL > 0:
            res.extend(intervals[:toMergeL])
        res.append(merged)
        if toMergeR < len(intervals) -1:
            res.extend(intervals[toMergeR+1:])
        return res

        
        t = newInterval
        
        class N:
            def __init__(self,i,j):
                self.start = i
                self.end = j

            def __init__(self):
                pass
        
        newInterval = N()
        newInterval.start = t[0]
        newInterval.end = t[1]

        s, e = newInterval.start, newInterval.end
        left = [N(i) for i in intervals if i.end < s]
        right = [N(i) for i in intervals if i.start > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)].start)
            e = max(e, intervals[~len(right)].end)
        return left + [Interval(s, e)] + right
        """
        
        s, e = newInterval[0], newInterval[1]
        right = [i for i in intervals if i[0] > e]
        left = [i for i in intervals if i[1] < s]
        print(left)
        print(right)
        if left + right != intervals:
            s = min(s, intervals[len(left)][0])
            #print(len(left))
            #print(~len(left))
            #rint(len(right))
            #print(~len(right))
            e = max(e, intervals[len(intervals) - len(right) -1][1])
        return left + [[s, e]] + right