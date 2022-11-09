class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:

        def getnum(num):
            s = str(num)
            total = 0
            for c in s:
                total += int(c)
            return total

        t= getnum(n)
        st = str(n)

        res = 0
        
        index = len(st) - 1
        rindex = 0
        
        while t > target:
            
            st = str(n)
            extra = (10 - int(st[index]) ) * (10**rindex)
            
            res += extra

            index -= 1
            rindex += 1
            
            n += extra

            t = getnum(n)

        return res

        return -1
