class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        def traverse(t):
            vis = [g.count(t) for g in garbage]
            while(vis and vis[-1] == 0):
                vis.pop()
            total = 0
            if not vis:
                return 0
            total += vis[0]
            for i in range(1,len(vis)):
                total += travel[i-1]
                total += vis[i]
            return total

        res = 0
        res += traverse('M')
        res += traverse('P')
        res += traverse('G')

        return res
