class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        c= Counter([l for w in words for l in w])

        L = len(words)
        for v in c.values():
            if v % L != 0:
                return False
        
        return True