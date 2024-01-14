from sortedcontainers import SortedList

class Trie:
    def __init__(self, *words):
        self.root = {}
        for word in words:
            self.add(word)

    def add(self, word):
        current_dict = self.root
        if not current_dict.get('#'):
            current_dict['#'] = SortedList()
        current_dict['#'].add(word)
        
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
            if not current_dict.get('#'):
                current_dict['#'] = SortedList()
            current_dict['#'].add(word)
        current_dict["_end_"] = True
    
    def g(self, word):
        res = []
        
        current_dict = self.root
        
        for letter in word:
            #print(current_dict)
            if letter not in current_dict:
                res.append([])
                current_dict = {}
                continue
            current_dict = current_dict[letter]
            res.append(current_dict['#'][0:3])
        #return current_dict['#'][0:3]
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
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie(*products)
        #print(t.root['#'])
        res = t.g(searchWord)
        rr = []
        for w in res:
            #print(w)
            rr.append(w)
        return rr