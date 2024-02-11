class Solution:
    def frequencySort(self, s: str) -> str:
        
        c = Counter(s)
        res = ''
        ll = [ (f,l) for l,f in c.items()]
        for k,v in sorted(ll, reverse=True):
            res += v * k

        return res
