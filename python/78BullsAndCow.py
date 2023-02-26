class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        s = list(str(secret))
        
        g = list(str(guess))
        

        extra2 = defaultdict(int)

        i = 0
        bull = 0
        for c in guess:
            if c == secret[i]:
                bull+=1
            else:
                extra2[secret[i]] += 1
            i+=1
        
        cow = 0
        i = 0

        for c in guess:
            if c != secret[i] and c in extra2 and extra2[c] >0:
                extra2[c] -= 1
                cow+=1
            
            i+=1

        return str(bull) + 'A'+ str(cow)+ 'B'




class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        list of characters
        
        """
        
        
        s = list(str(secret))
        
        g = list(str(guess))
        
        
        i = 0
        cow = 0
        bull = 0
        m = defaultdict(int)
        for c in s:
            if c == g[i]:
                bull += 1
            else:
                m[c] += 1
            i+= 1

        i = 0
        for c in g:
            if c != s[i] and c in m and m[c] > 0:
                m[c] -= 1
                cow += 1
            i+= 1

        return str(bull) + 'A'+ str(cow)+ 'B'
        
        
        s, g = Counter(secret), Counter(guess)
    #a = sum(i == j for i, j in zip(secret, guess))
    #return '%sA%sB' % (a, sum((s & g).values()) - a)

    #return '%sA%sB' % (a, sum((s & g).values()) - a)


    def getHint(self, secret, guess):
    bulls = sum(map(operator.eq, secret, guess))
    both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
    return '%dA%dB' % (bulls, both - bulls)