class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        

        @cache
        def dp(i, available):
            
            if i == len(words):
                return 0
        
            res = dp(i+1,available)
            
            new_available = list(available)
            sc = 0
            for l in words[i]:
                new_available[ord(l)-ord('a')] -= 1
                sc += score[ord(l)-ord('a')]
                if new_available[ord(l)-ord('a')] < 0:
                    return res
            
            res = max(res, dp(i+1, tuple(new_available)) + sc)
            
            return res
        
        start = [0]*26

        for l in letters:
            start[ord(l)-ord('a')]+=1
        start = tuple(start)

        return dp(0, start)