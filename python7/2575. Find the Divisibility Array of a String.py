class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        
        count = 0
        
        res = []
        for w in word:
            count *= 10
            count += int(w)
            if count > m : 
                count = count % m
            res.append(0 if count % m != 0 else 1)
        
        return res