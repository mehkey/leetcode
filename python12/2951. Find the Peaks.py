class Solution:
    def findPeaks(self, m: List[int]) -> List[int]:

        mm = len(m)

        res = []
        for i in range(1,mm-1):
            
            if m[i-1] < m[i] > m[i+1]:
                res.append(i)

        return res
