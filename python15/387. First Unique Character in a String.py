class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)

        for i,cc in enumerate(s):
            if c[cc] == 1:
                return i
        return -1