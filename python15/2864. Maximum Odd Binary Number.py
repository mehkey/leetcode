class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        l = len(s)

        c = s.count('1')
        
        res = []

        for _ in range(c-1):
            res.append('1')
        
        for _ in range(l-c):
            res.append('0')
        
        res.append('1')

        return ''.join(res)
        
        ones_count = s.count("1")
        zeros_count = len(s) - ones_count

        return "1" * (ones_count - 1) + "0" * zeros_count + "1"