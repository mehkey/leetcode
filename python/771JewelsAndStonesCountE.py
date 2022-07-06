class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        #print(list(J.count))
        #print(S)
        #print(list(map(J.count, S)))
        #print(list(map(S.count, J)))

        #return sum(map(J.count, set(S)))
    
        #return sum(map(S.count, J))
        #j = set(J)
        #return sum( S.count(jewel) for jewel in J )
        #jewel = set(J)
        #return sum( [1 for item in S if item in jewel ] )
        #return sum(s in j for s in S)
        
        j = set(J)
        return sum(s in j for s in S)
    
        #a, b = Counter(S), Counter(J)

        #print(list(map(a.get,b) or [0]))
        #return sum(map(a.get,b))
        
        # https://leetcode.com/problems/jewels-and-stones/discuss/527360/Several-Python-solution.-w-Explanation