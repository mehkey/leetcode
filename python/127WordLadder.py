class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList.append(beginWord)
        
        graph = {}
        for word in wordList:
            graph[word] = []
        
        def compare(word,word2):
            count = 0
            for char1,char2 in zip(word,word2):
                if char1 !=char2:
                    count += 1
            return count == 1
            
        
        for word in wordList:
            for word2 in wordList:
                if word != word2 and compare(word,word2):
                    graph[word].append(word2)
            
        #O(n squared)
        
        queue = deque()
        
        queue.append(beginWord)
        queue.append("@")
        
        counter = 1
        visited = set()

        print(graph)
        while True:
            
            if len(queue) == 1 and queue.peek == "@":
                return 0
            
            word = queue.popleft()
            
            if word == "@":
                counter += 1
                queue.append("@")
            else:
                
                if word == endWord:
                    return counter
                
                if not word in visited:
                    for nextWord in graph[word]:
                        queue.append(nextWord)
            
        
        return 0
                    
        #O(n2)
        #O(n)
        
        

