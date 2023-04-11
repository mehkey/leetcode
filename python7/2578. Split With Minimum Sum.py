class Solution:
    def splitNum(self, num: int) -> int:

        num = list(str(num))

        num.sort()

        n1 = 0

        n2 = 0

        b = True

        for n in num:
            
            if b:
                n1 *= 10
                n1 += int(n)
            else:
                n2 *= 10
                n2 += int(n)
            
            b = not b

        return n1 + n2