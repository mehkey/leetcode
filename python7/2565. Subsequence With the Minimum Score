class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        sl = 0
        sr = len(s) - 1
        tl = 0
        tr = len(t) - 1
        k = {}
        for tl in range(len(t)):
            while sl < len(s) and s[sl] != t[tl]:
                sl += 1
            if sl == len(s):
                tl -= 1
                break
            # save smallest sleft for all left
            k[tl] = sl
            sl += 1
            
        # we set left = -1, when we don't use left
        k[-1] = -1
        ans = tr - tl
        # iterate every left by decreasing one
        # releave the limitation of s[sleft:]
        for ntl in range(tl, -2, -1):
            # every time we decrease left, check if right can be decreased
            while tr > ntl and sr > k[ntl]:
                if s[sr] != t[tr]:
                    sr -= 1
                elif s[sr] == t[tr]:
                    sr -= 1
                    tr -= 1
            ans = min(tr - ntl, ans)
        return ans