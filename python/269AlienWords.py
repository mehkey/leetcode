from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        
        graph = { c:set() for w in words for c in w}

        for i in range(len(words)-1): #skip the last

            word1,word2 =  words[i], words[i+1]

            minlength = min(len(word1),len(word2))

            if len(word1) > len(word2) and word1[:minlength] == word2[:minlength]:
                return ""

            for j in range(minlength):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break



        visited = {}

        res = []

        #BFS # queue loop 
        #DFS # stack or recursive
        print(graph)
        def dfs(letter):
            
            if letter in visited:
                return visited[letter]

            currentSet = graph[letter]

            visited[letter] = True
            for adjacentLetter in currentSet:
                if dfs(adjacentLetter):
                    return True
            visited[letter] = False
    
            res.append(letter)


        for letter in graph:
            if dfs(letter):
                return ""

        res.reverse()
        return "".join(res)