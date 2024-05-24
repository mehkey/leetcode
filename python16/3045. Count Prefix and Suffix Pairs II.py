
class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, w, reverse=False):
        cur = self.root
        indices = set()
        for c in w:
            if c in cur:
                cur = cur[c]
            else:
                cur[c] = {}
                cur = cur[c]
            if 'end' in cur:
                indices.add(cur['end'])
        cur['end'] = w[::-1] if reverse else w
        return indices

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pref = Trie()
        suf = Trie()
        ct = defaultdict(int)
        res = 0
        for w in words:
            indices1 = pref.insert(w)
            rw = w[::-1]
            indices2 = suf.insert(rw, True)
            
            for j in indices1 & indices2:
                res += ct[j]

            ct[w] += 1
        return res


def isp(s1,s2):
    if len(s1) > len(s2):
        return False

    if s1 == s2[:len(s1)] and s1 == s2[len(s2) - len(s1):] :
        return True

    return False

class Trie:
    def __init__(self, *words):
        self.root = {}
        for word in words:
            self.add(word)

    def add(self, word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict["_end_"] = current_dict.get("_end_",0) + 1
    
    def check(self, word):
        current_dict = self.root
        res = 0
        N = len(word)

        current_dict2 = self.root
        
        for i,letter in enumerate(word):
            cr = word[N-1-i]

            if "_end_" in current_dict: #and isp(): # and "_end_" in current_dict2:
                res += current_dict["_end_" ]

            if letter not in current_dict or cr not in current_dict2:
                return res

            current_dict = current_dict[letter] #current_dict.setdefault(letter, {})
            current_dict2 = current_dict2[cr] #current_dict2.setdefault(cr, {})

        if "_end_" in current_dict and "_end_" in current_dict2:
            res += current_dict["_end_" ]
        
        return res
        
    
    def __contains__(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return "_end_" in current_dict

    def __delitem__(self, word):
        current_dict = self.root
        nodes = [current_dict]
        for letter in word:
            current_dict = current_dict[letter]
            nodes.append(current_dict)
        del current_dict["_end_"]

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        T = lambda: defaultdict(T)
        root = T()
        res = 0
        for w in words:
            x = root
            for k in zip(w, reversed(w)):
                x = x[k]
                res += x.get(0, 0)
            x.setdefault(0, 0)
            x[0] += 1
        return res
        
        '''
        def isp(s1,s2):
            
            if s1 == s2[:len(s1)] and s1 == s2[len(s2) - len(s1):] :
                return True
            
            return False

        N = len(words)
        
        res = 0
        
        hm = defaultdict(set)

        for i in range(N):
            s = words[i]
            cur = []
            
            for k in range(len(s)):
                cur.append(s[k])
                jc = ''.join(cur)
                if isp(jc,s):
                    hm[s].add(jc)

        cc = set()
        cs = defaultdict(int) #set()
        res = 0
        '''
        t = Trie()
        tt = Trie()
        N = len(words)
        
        res = 0
        for i in range(N):
            word = words[i]
            #for w in  cc & hm[words[i]] :
            #    res += cs[w] #len( cs & hm[words[i]] )
            res +=  t.check(word) #( t.check(word) +  tt.check(word) ) 

            t.add(word)
            #tt.add(word[::-1])

        return res # // 2

        #eturn 0
        
        #for i in range(N):
        #    for j in range(i+1,N):
        #        if isp(words[i],words[j]) :
        #            res += 1
        
        def dfs(n):
            
            cur = words[n]
            
            for i in range(n+1,N):
                pass
        
        return dfs(0)
    
        '''
        
        ababa -> ababa , aba, a

        def isp(s1,s2):
            if len(s1) > len(s2):
                return False
            
            if s1 == s2[:len(s1)] and s1 == s2[len(s2) - len(s1):] :
                return True
            
            return False
        
        res = 0
        for i in range(N):
            for j in range(i+1,N):
                if isp(words[i],words[j]) :
                    res += 1

        return res
        '''