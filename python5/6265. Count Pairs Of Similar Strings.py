class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        sol = defaultdict(int)
        pair = 0
        for w in words:
            
            hm = tuple(sorted(list(set(w))))
            if hm not in sol:
                sol[hm] = 1
            else:
                pair += sol[hm]
                sol[hm] +=1 
        
        return pair