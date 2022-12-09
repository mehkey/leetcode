'''
class Trie:
    
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        t = self.trie
        for c in word:
            if c not in t: t[c] = {}
            t = t[c]
        t["-"] = True

    def search(self, word: str, miss: int) -> bool:
        t = self.trie
        pos = 0
        if word == "iarapqqk":
            print("HERE!")
        if word == "larapqqk":
            print("HERE!!")
        if word == "larakqqk":
            print("HERE!!!")

        for i,c in enumerate(word):
            if c not in t:
                if miss <= 0:
                    #if word == "iarapqqk":
                    #    print("HERE")
                    return False
                else:
                    #if word == "iarapqqk":
                    #    print("MISS", miss)
                    for v in t:

                        s = word[:i] + v + word[i+1:]
                        if word == "iarapqqk":
                            print("MISS new word", s)

                        if self.search(s, miss -1):
                            return True

                    return False
                        
            t = t[c]
            pos += 1
                  
        return "-" in t
        
        t = Trie()
        
        for word in dictionary:
            t.insert(word)

'''

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        

        def match(word:str,d):
            t = 0
            m = 2
            for i,w in enumerate(word):
                if w != d[i]:
                    m -=1
                
                if m == -1:
                    return False

            return True

        res = []

        for word in queries:

            for d in dictionary:
                if match(word, d):
                    res.append(word)
                    break

        return res