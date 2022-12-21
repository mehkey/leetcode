
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return abs(stones[0] - stones[1])

        # to simplify logic below
        if len(stones) % 2 == 0:
            stones.append(stones[-1] + 1)

        j = 0

        # -> go forward
        for i in range(0, len(stones) - 2, 2):
            j = max(j, abs(stones[i] - stones[i+2]))

        # <- go backward
        for i in range(1, len(stones) - 2, 2):
            j = max(j, abs(stones[i] - stones[i+2]))

        return j

class Solution:
    def maxJump(self, stones: List[int]) -> int:

        def dp(i, forward, visited):

            if i == len(stones) -1 and forward:
                
                return dp(i, False, visited)
            
            if i == 0 and not forward:
                return 0
            
            visited.add(i)
            new_m = 0
            
            if forward:
                for j in range(i+1,len(stones)):
                    if j not in visited:
                        new_m = max(stones[j] - stones[i], new_m)
                        new_m = max(dp(j, i+1, visited), new_m)
            
            if not forward:
                for j in range(i-1,-1,-1):
                    if j not in visited:
                        new_m = max(stones[i] - stones[j], new_m)
                        new_m = max(dp(j, i-1, visited), new_m)

            visited.remove(i)

            return new_m
        
        return dp(0,True,set())