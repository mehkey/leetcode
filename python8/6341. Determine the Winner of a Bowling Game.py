class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        
        p1 = 0
        
        for i,v in enumerate(player1):
            m = 1
            if i >=1 and player1[i-1] == 10:
                m =2
            if i >=2 and player1[i-2] == 10:
                m =2
            
            
            p1 += m*v 
        
        p2 = 0
        
        for i,v in enumerate(player2):
            m = 1
            if i >=1 and player2[i-1] == 10:
                m =2
            if i >=2 and player2[i-2] == 10:
                m =2
            p2 += m*v 
            
        if p1 > p2:
            return 1
        elif p2 > p1:
            return 2
        else:
            return 0

def isWinner(p1: List[int], p2: List[int]) -> int:
    ans, s1, s2 = 0, 0, 0
    n = len(p1)
    for i in range(n):
        s1 += p1[i]
        s2 += p2[i]
    if n > 1:
        for i in range(1, n):
            if p1[i - 1] == 10 or ((i >= 2) and p1[i - 2] == 10):
                s1 += p1[i]
            if p2[i - 1] == 10 or ((i >= 2) and p2[i - 2] == 10):
                s2 += p2[i]
    if s1 == s2:
        ans = 0
    elif s1 > s2:
        ans = 1
    else:
        ans = 2
    return ans


class Solution:
    def isWinner(self, player_a: List[int], player_b: List[int]) -> int:
        score_a = self.get_score(player_a)
        score_b = self.get_score(player_b)

        return {
            score_a > score_b: 1,
            score_a < score_b: 2,
        }.get(True, 0)

    @staticmethod
    def get_score(player: List[int]) -> int:
        score = 0

        for i, sc in enumerate(player):
            if i > 0 and player[i - 1] == 10:
                score += 2 * sc
            elif i > 1 and player[i - 2] == 10:
                score += 2 * sc
            else:
                score += sc

        return score