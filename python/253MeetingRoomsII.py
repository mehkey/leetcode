def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        startTime = invervals.sort(key=lambda x : x[0]).copy()
        endTime = intervals.sort(key=lambda y: y[1]).copy()

        s = 0
        e = 0
        count = 0
        maxC = 0
        while s < len(intervals) :
            if startTime[s] <= endTime[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            maxC = max(maxC, count)
        return maxC
        