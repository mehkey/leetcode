class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        c = Counter(s)
        
        tt = Counter(t)

        diff = 0
        #
        for i in range(26):
            diff += abs( c[chr(i+ord('a'))] -tt[chr(i+ord('a'))])
        
        return diff//2
        #diff = sum()
