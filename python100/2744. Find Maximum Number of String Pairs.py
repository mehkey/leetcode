class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        '''
        hm = defaultdict(int)

        for word in words:

            wl = [c for c in word]
            #w1 = wl[::]
            wl.reverse()

            hm[tuple(wl)] += 1
            
            wl.reverse()
            hm[tuple(wl)] += 1

        '''
        
        s = list(words)
        
        c = 0
        
        for w in words:
            
            s.remove(w)
            
            rev = w[::-1]
            
            if rev in s:
                c+=1
                s.remove(rev)
                
            else:
                s.append(w)

        return c
