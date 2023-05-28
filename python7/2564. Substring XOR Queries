class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        seen = {}
        for i, ch in enumerate(s):
            if ch == '1': 
                val = 0
                for j in range(i, min(len(s), i+30)): 
                    val <<= 1
                    if s[j] == '1': val ^= 1
                    seen.setdefault(val, [i, j])
            else: seen.setdefault(0, [i, i])
        return [seen.get(x^y, [-1, -1]) for x, y in queries]