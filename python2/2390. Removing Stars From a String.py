class Solution:
    def removeStars(self, s: str) -> str:

        res = []

        for c in s:
            res.append(c)
            
            if res[-1] == '*':
                res.pop()
                if res:
                    res.pop()

        return ''.join(res)
