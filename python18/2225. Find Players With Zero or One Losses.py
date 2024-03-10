class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        

        res = []

        win = []
        los = []

        lc = Counter()
        ls = set()
        al = set()

        for w,l in matches:
            ls.add(l)
            lc[l] += 1
            al.add(w)
            al.add(l)

        return [  sorted(list( al - ls )),  sorted([p for p,m in lc.items() if m == 1])  ]