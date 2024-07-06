lis = []

for i in range(1,10):
    cur = i
    lis.append(cur)
    for j in range(0,9):
        prev = cur %10
        if prev < 9:
            cur *= 10
            cur += prev + 1
            lis.append(cur)

lis.sort()

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        l = bisect_left(lis,low)
        
        r = bisect_right(lis,high)
        
        res = []
        for val in range(l,r+1):
            if val < len(lis) and low <= lis[val]<= high:
                res.append(lis[val])
                
        return res