class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        
        if not words:
            return []

        res = 0
        cur = groups[0]
        res = []
        res.append(words[0])
        
        for i in range(1,n):
            if groups[i] != cur:
                res.append(words[i])
                cur = groups[i]
            else:
                pass
        
        return res