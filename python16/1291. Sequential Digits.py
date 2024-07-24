lis = []

for c in range(1,9):
    cur = []
    cc = c
    for k in range(c,10):
        cur.append(str(k))
        lis.append(int(''.join(cur)))

lis.sort()

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        c = "123456789"
        a = []

        for i in range(len(c)):
            for j in range(i + 1, len(c) + 1):
                curr = int(c[i:j])
                if low <= curr <= high:
                    a.append(curr)

        a.sort()
        return a
        l = bisect_left(lis,low)
        r = bisect_right(lis,high)

        return lis[l:r]