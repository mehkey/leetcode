class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        @cache
        def heights(num):
            cur = 0
            while num > 1:
                num = num // 2
                cur +=1
            return cur

        
        @cache
        def par(n1,n2):
            
            if n1 > n2:
                return par(n2,n1)

            no1 = heights(n1)

            while heights(n2) != heights(n1):
                n2 = n2 // 2
                
            while heights(n1) != 0 and n1 != n2:
                n1 = n1 //2
                n2 = n2 //2
            return heights(n1)

        
        hmm = {}
        res = []
        for q in queries:
            if tuple(sorted(q)) not in hmm:
                hmm[tuple(sorted(q)) ] = heights(q[0]) + heights(q[1]) + 1 - 2*par(q[0],q[1]) 

            res.append(hmm[tuple(sorted(q))])

        return res