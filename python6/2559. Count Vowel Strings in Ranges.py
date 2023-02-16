class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        v = set({'a','e','i','o','u'})
        t = [0] * len(words)
        for i,w in enumerate(words):
            
            if i>0:
                t[i] = t[i-1]
            
            if w[0] in v and w[-1] in v:
                t[i] += 1
                
        res = []
        for q in queries:
            if q[0] -1 >=0:
                res.append( t[q[1]] - t[q[0]-1])
            else:
                res.append( t[q[1]])
        
        return res