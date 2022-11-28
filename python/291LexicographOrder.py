class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def lexo(letter):
            if len(letter) == 0:
                return 0
            l = 25
            for i in letter:
                l = min(l,ord(i) - ord('a')) 
            c = Counter(letter)
            #print(chr(l + ord('a')))
            return c[chr(l + ord('a')) ]
        
        #print(lexo(queries[0]))
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
        
        
        class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = sorted(w.count(min(w)) for w in words)
        return [len(f) - bisect.bisect(f, q.count(min(q))) for q in queries]


        

