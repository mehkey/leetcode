class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        
        if num == 0:
            return True

        n = len(str(num-1))
 
        n -=2

        if n < 0:
            n = 0

        for i in range(10**(n), 10**(n+2)):
            if i + int(str(i)[::-1]) == num:

                return True
        
        return False