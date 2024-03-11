class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        N= len(s)
        h1= s[:N//2]
        h2 = s[N//2:]

        c1 = sum(c in 'aeiouAEIOU' for c in h1)
        c2 = sum(c in 'aeiouAEIOU' for c in h2)
  
  
        return c1 == c2