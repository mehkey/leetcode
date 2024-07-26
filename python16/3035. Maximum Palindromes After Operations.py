
class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        cnt, res = Counter([ch for w in words for ch in w]), 0
        pairs = sum(char_cnt // 2 for char_cnt in cnt.values())
        for sz in sorted([len(w) for w in words]):
            pairs -= sz // 2
            res += pairs >= 0
        return res
        
        
        c = Counter()

        for w in words:

            for cc in w:
                c[cc] += 1

        ex = 0
        pa = 0

        for l in c:
            if c[l] % 2 == 1:
                ex += 1
                pa -= 1
            pa += c[l] 

        lens = [len(w) for w in words]

        ans = 0
        
        tot = ex + pa

        for l in sorted(lens):
            
            if l % 2 == 1:
                ll = l - 1
                if tot - ll - 1 >= 0 and ll <= pa: 
                    pa -= ll 
                    
                    tot -= l

                    ans += 1

                    if ex == 0:
                        pa -= 1
                        ex = 1
                    else:
                        ex -= 1
                        
            else:
                if l <= pa:
                    pa -= l
                    ans += 1
                    tot -= l

        return ans