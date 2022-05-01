from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x : x.start)
        startTime = intervals.copy()
        intervals.sort(key=lambda y : y.end)
        endTime =  intervals.copy()

        s = 0
        e = 0
        count = 0
        maxC = 0
        while s < len(intervals) :
            if startTime[s].start < endTime[e].end:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            maxC = max(maxC, count)
        return maxC


        




