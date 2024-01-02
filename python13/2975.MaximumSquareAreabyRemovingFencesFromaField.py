class Solution:
    def maximizeSquareArea(self, m: int, n: int, hBars: List[int], vBars: List[int]) -> int:

        maxCont = 0
        curCont = 0

        hBars.sort()
        vBars.sort()

        svet = set()
        shor = set()

        prev = [1]
        for h in hBars:

            for pp in prev:
                shor.add(h-pp)

            prev.append(h)

        for pp in prev:
            shor.add(m-pp)

        maxCont2 = 0
        curCont = 0

        prev =[ 1]
        for v in vBars:

            for pp in prev:
                svet.add(v-pp)
            prev.append(v)

        for pp in prev:
            svet.add(n-pp)
        com = svet & shor

        if not com:
            return -1
        
        return pow(max(com),2, 10**9+7)
