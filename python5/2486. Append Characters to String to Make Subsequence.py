class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        S = len(s)
        T = len(t)
        
        tot = 0
        count = 0
        
        for i in range(S):
            
            if s[i] == t[count]:
                count += 1
            
            if count == T:
                break

        return T - count
        