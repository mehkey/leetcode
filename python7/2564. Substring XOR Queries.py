def substringXorQueries(self, s, queries):
        res = []
        for fir, sec in queries:
            x = bin(sec ^ fir)[2:]
            i = s.find(x)
            res += [[-1, -1]] if i < 0 else [[i, i + len(x) - 1]]
        return res


class Solution:
    def substringXorQueries(self, s: str, v: List[List[int]]) -> List[List[int]]:
        def cmp():
            return -2
        ans=[]
        mp=defaultdict(cmp)
        for i in v:
            x=bin((i[0]^i[1]))[2:]
            if mp[x]!=-2:
                if mp[x]==-1:
                    ans+=[[-1,-1]]
                else:
                    ans+=[[mp[x],mp[x]+len(x)-1]]
                continue 
            y=s.find(x)
            if y==-1:
                ans+=[[-1,-1]]
            else:
                ans+=[[y,y+len(x)-1]]
            mp[x]=y
        return ans

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


def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        dt, n = {}, len(s)
        for i in range(n):
            t = 0
            for j in range(i, min(i + 30, n)):
                t = (t << 1) | int(s[j])
                if t not in dt or dt[t][1] - dt[t][0] > j - i:
                    dt[t] = [i, j]
            
        return [dt.get(fir ^ sec, [-1, -1]) for fir, sec in queries]