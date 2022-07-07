class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        """
        def lexo(letter):
            if len(letter) == 0:
                return 0
            l = 25
            for i in letter:
                l = min(l,ord(i) - ord('a')) 
            c = Counter(letter)
            return c[chr(l + ord('a')) ]
        
        lis = []
        for w in words:
            lis.append(lexo(w))

        res = []
        for q in queries:
            count = 0
            lex = lexo(q)
            for l in lis:
                if lex < l:
                    count+=1
            res.append(count)

        return res
        """
        
        def f(s):
            t = sorted(list(s))[0]
            return s.count(t)
        
        query = [f(x) for x in queries]
        word = [f(x) for x in words]
        m = []
        for x in query:
            count = 0
            for y in word:
                if y>x:
                    count+=1
            m.append(count)
        return m
        