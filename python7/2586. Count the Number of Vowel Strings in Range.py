class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        
        v = "aeiou"
        
        c = 0
        for i in range(left,right+1):
            if words[i] and words[i][0] in v and words[i][-1] in v:
                c+=1
        
        return c