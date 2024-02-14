class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:

        w = word

        change = 0

        while True:

            if len(w) >= k:
                w = w[k:] 
            else:
                w = ''

            change += 1
            if w == '' or w == word[:  len(w)]:
                return change
        
        return -1

        '''
        
        def match(st, hm):
            for w in st:
                hm[w] -=1
            
            for k in hm:
                if hm[k] != 0:
                    return False

            return True
        
        def dp(start, hm):
            if not start:
                return 1
            
            if start == word[:len(start)] and match(word[len(start):],hm):
                return 1
            
            #for c in word[]
            
            return 0
            
        
        
        return dp(word[:k], Counter())



        w = word
        change = 0
        
        chm = Counter()
        
        while True:
            #for c in w[:k]:
                #chm += 
            #print(w[k:] , w[:k])
            w = w[k:] #+ w[:k]
            #for c in 
            #print()
            change += 1
            if w == word:
                return change
        
        return -1
        
        '''