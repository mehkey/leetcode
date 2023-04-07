class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        N = len(reward1)

        bind = [[r1 - r2, r1, r2] for r1,r2 in zip(reward1,reward2)]
        bind.sort(key=lambda x: -x[0])

        res = 0
        

        for i in range(k):
            res += bind[i][1]
        
        for i in range(k, N):
            res += bind[i][2] 
        return res