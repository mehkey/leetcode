class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        """
        
        
        divisor   2   4.   8.  16  32.   64.   128
        
        times     1   2.   4.  8.  16.   32.   64 
        
        
        dividend 450
        
        remove from the dividend
        
        448 -> 
        
        """

        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        current = 0
        res = 0

        while dividend >= divisor: #O(logn)
            temp, i = divisor, 1
            while dividend >= temp: #O(logn)
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1

        if not positive:
            res = -res
        return min(max(-2**31, res), 2**31-1)
        
        
        
        
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
                
        if not positive:
            res = -res
        return min(max(-2*31, res), 2**31-1)
        """
        

        i, res = 0, 0 # Initialize stuff.

        while divisor << i <= dividend:
            i += 1 # Phase 1: Figure out how far left you should go.

        for j in reversed(range(i)): # Phase 2: Divide like a 7-year-old.
            if divisor << j <= dividend:
                dividend -= divisor << j
                res += 1 << j
        
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)






        i, res = 0, 0 # Initialize stuff.

        current = divisor
        while current <= dividend:
            i += 1 # Phase 1: Figure out how far left you should go.
            current = current << 1

        for j in reversed(range(i)): # Phase 2: Divide like a 7-year-old.
            current = divisor << j
            if current <= dividend:
                dividend -= current
                res += 1 << j
        
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)
        