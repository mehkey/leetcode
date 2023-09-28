class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        #ma= max([y for x,y in nums])
        #m= min([x for x,y in nums])
        s = set()
        
        for x,y in nums:
            for i in range(x,y+1):
                if i not in s:
                    s.add(i)
        return len(s)
        #for i in range(m,ma+1):
