class Solution:
    def countDaysTogether(self, aa: str, la: str, ab: str, lb: str) -> int:

        aa = aa.split('-')
        la = la.split('-')
        ab = ab.split('-')
        lb = lb.split('-')
        
        start1 = date(2013,int(aa[0]),int(aa[1]))
        end1 = date(2013,int(la[0]),int(la[1]))
        start2 = date(2013,int(ab[0]),int(ab[1]))
        end2 = date(2013,int(lb[0]),int(lb[1]))
        
        overlaps = start1 <= end2 and end1 >= start2
        if not overlaps:
            return 0
        return abs(max(start1, start2)-min(end1, end2)).days +1
        
