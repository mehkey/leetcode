class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        class TrieNode():
            def __init__(self):
                self.children = defaultdict(TrieNode)
                self.isWord = False
                self.count = 0

        class Trie():
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word):
                node = self.root
                for w in word:
                    node.count += 1
                    node = node.children[w]
                node.count += 1
                node.isWord = True
            
            def searchCC(self, word):
                tot = 0
                node = self.root
                for w in word:
                    node = node.children.get(w)
                    if not node:
                        return tot
                    tot += node.count
                return tot

        t = Trie()
        
        for w in words:
            t.insert(w)
        r = []
        for w in words:
            r.append( t.searchCC(w) )
        return r