class Solution:
    def lastNonEmptyString(self, s: str) -> str:

        
        

        hm = defaultdict(int)
        
        cc = Counter(s)
        
        m = max(cc.values())
        
        res = []
        
        used = set()

        for c in reversed(s):
            if cc[c] == m and c not in used:
                used.add(c)
                res.append(c)

        return ''.join(reversed(res))



class Solution {
    public String lastNonEmptyString(String s) {
        int[] cnt = new int[26];
        int mx = 0;
        for (int i = 0; i < s.length(); ++i) {
            mx = Math.max(mx, ++cnt[s.charAt(i) - 'a']);
        }
        var last = new StringBuilder();
        var seen = new HashSet<>();
        for (int i = s.length() - 1; i >= 0; --i) {
            char c = s.charAt(i);
            if (mx == cnt[c - 'a'] && seen.add(c)) {
                last.append(c);
            }
        }
        return last.reverse().toString();
    }
}