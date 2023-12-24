class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        maxCont = 0
        curCont = 0
        
        hBars.sort()
        vBars.sort()
        
        prev = -inf
        for h in hBars:

            if h - prev ==1:
                curCont += 1
            else:
                curCont = 1
            prev= h
            maxCont = max(maxCont, curCont)

        maxCont2 = 0
        curCont = 0

        prev = -inf
        for h in vBars:

            if h - prev ==1:
                curCont += 1
            else:
                curCont = 1
            prev= h
            maxCont2 = max(maxCont2, curCont)

        return (min(maxCont,maxCont2) + 1 ) ** 2
