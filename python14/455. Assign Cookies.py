class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        
        g.sort()
        s.sort()
        s = deque(s)
        i = 0

        while i < len(g):
            while s and s[0] < g[i]:
                s.popleft()
            if not s:
                break
            if g[i] <= s[0]:
                s.popleft()
                i+=1
            else:
                break

        return i