

class Solution:
    def __init__(self):
        self.x = None

    def price(self, num):
        res = 0
        for i in range(self.x - 1, 64, self.x):
            numModTwoTimesI = num % (1 << (i + 1))
            res += ((num - numModTwoTimesI) >> 1) + max(numModTwoTimesI - (1 << i), 0)
        return res
    
    def findMaximumNumber(self, k: int, x: int) -> int:
        self.x = x
#        return bisect_right(range((1 << 63) - 1), k, key=self.price) - 2

        return bisect_right(range((1 << 63) - 1), k, key=self.price) - 2

    #def findMaximumNumber2(self, k: int, x: int) -> int:
    #    self.x = x
    #    return bisect_right(range((1 << 63) - 1), k, key=self.price) - 2

    def findTheLast(self) -> int:
        return 0

