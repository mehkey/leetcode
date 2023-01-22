class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = collections.defaultdict(list)
        for c, p in enumerate(parent):
            tree[p].append(c)

        self.ret = 1
        @cache
        def calc(node):
            temp = []
            for c in tree[node]:
                sub = calc(c)
                if s[node] != s[c]:
                    temp.append(sub)
            temp.sort()
            if len(temp) >= 2: 
                self.ret = max(self.ret, 1 + temp[-1] + temp[-2])
            elif temp: 
                self.ret = max(self.ret, 1 + temp[-1])
            return 1 if not temp else (1 + temp[-1])
        calc(0)
        return self.ret