class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l = []

        for i in range(len(colors)):
            if i == 0 or colors[i] != colors[i-1]:
                l.append([])
            l[-1].append(neededTime[i])

        res = 0
        #print(l)
        for x in l:
            res += sum(x) - max(x)

        return res
