class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        lettersCount = {}
        longest = 0
        
        for r in range(len(s)):
            
            lettersCount[s[r]] = 1 + lettersCount.get(s[r],0)
            
            while r - l + 1  - max(lettersCount.values()) > k:
                lettersCount[s[l]] -= 1 
                l += 1
            
            longest = max(longest, r - l +  1)
        
        return longest
        