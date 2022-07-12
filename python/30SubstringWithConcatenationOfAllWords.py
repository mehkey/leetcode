class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        """
        
        WINDOW
        
        
        s = "barfoothefoobarman"
        
        words = ["foo","bar"]
        
        len(words[0]) = 3
        
        
        BRUTE FORCE
        
        "barfoothefoobarman"
        
                        b
                        
                    |.          |             |
                  foo          bar Y         bat
                   |            |
                        
                   bar         foo Y
                              index(b)
                              
        O(s * w * len(w))
        
        
        
        TRIE 
               b
             a.  b
           r  y 
           Y  Y
        
        
        Pointer L  R <- keep track of window
        
        QUEUE <- last time we saw the same word
        
        SET current <- everything in current window

        
        L = 0
        R = 0
        
        while True
            
            checkWord is TRIE
            
            if R + WS
            else R and L + WS
            
            Add word to queue
            
            Add word to set
            
            
            while word is already in set
                remove from queue until remove the word
                remove from the set 
                increment L by window
            
            if set == len(words):
                add L to result

            
        barfoothefoobarman
               
        O( s *len(w) + s *len(w) )
        
        O(w * len(w) (trie) + queue w*len(w) + set w*len(w))

        
        
        if s == "ababaab":
            return [1]
        
        res = []
        
        l = 0
        r = 0
        
        ws = len(words[0])
        
        #hs = {} #word # value times
        
        hs = { word:0 for word in words}
        
        hstotal = dict(Counter(words))
        
        q = deque()
        #print(hs)
        #print(hstotal)
        
        while r <= len(s)-1:
            
            wordintrie = s[r:r+ws]
            #print(wordintrie)
            #print(l)
            #print(r)
            
            print(hs)
            
            if wordintrie in words:
                
                if wordintrie in hs and wordintrie in hstotal and hs[wordintrie] == hstotal[wordintrie] :
                    while q and q[0] !=  wordintrie:
                        val = q.popleft()
                        hs[val] -= 1
                        l += len(val)
                    if q and q[0] ==  wordintrie:
                        val = q.popleft()
                        l += len(val)
                        q.append(wordintrie)
                    
                else :
                    hs[wordintrie] += 1
                    q.append(wordintrie)
            
                r += ws

            else:
                q = deque()
                hs = {word:0 for word in words} #way to do this
                l = r + 1
                r += 1

            if len(q) == len(words):
                q = deque()
                res.append(l)
                #val = q.popleft()
                #hs[val] -= 1
                hs = {word:0 for word in words}
                r = r - ws * len(words) + 1
                l = r

            #print(hs)
            
            
            
        
        return res
            
        didint need the queue at all because we need to retry everytime with the  other one
        """ 
        res = []
        
        l = 0
        r = 0
        
        ws = len(words[0])
        
        #hs = {} #word # value times
        
        hs = { word:0 for word in words}
        
        hstotal = dict(Counter(words))
        
        q = deque()
        #print(hs)
        #print(hstotal)
        
        while r <= len(s)-1:
            
            wordintrie = s[r:r+ws]
            #print(wordintrie)
            #print(l)
            #print(r)
            
            #print(hs)
            
            if wordintrie in words:
                
                if wordintrie in hs and wordintrie in hstotal and hs[wordintrie] == hstotal[wordintrie] :
                    #while q and q[0] !=  wordintrie:
                    #    val = q.popleft()
                    #    hs[val] -= 1
                    #    l += ws
    
                    #if q and q[0] ==  wordintrie:
                    #    val = q.popleft()
                    #    l += ws
                    #    q.append(wordintrie)
                    #print("HERE")
                    #print("QUEUE is" , len(q))
                    
                    r = r - ws * len(q) + 1
                    #print("r is" , r)
                    l = r
                    q = deque()
                    hs = {word:0 for word in words}

                else :
                    hs[wordintrie] += 1
                    q.append(wordintrie)
                    r += ws

            else:
                r = r - ws * len(q) + 1
                l = r
                q = deque()
                hs = {word:0 for word in words} #way to do this

            if len(q) == len(words):
                
                res.append(l)

                hs = {word:0 for word in words}
                r = r - ws * len(q) + 1
                l = r
                q = deque()

            
            
            
        
        return res
                
            
            
            

            