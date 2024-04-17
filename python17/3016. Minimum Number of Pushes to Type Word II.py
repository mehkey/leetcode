class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        
        
        i = 0
        count = 1
        
        res = 0
        
        for v,k in sorted([[v,k] for k,v in c.items()], reverse=True):
            
            res += v * count
            
            i+=1
            if i % 8 == 0:
                count += 1
        
        return res