class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        
        
        """
        
        GRAPH
        
        words
        Hashamp -> List
        hit -> [ hot]
        hot -> [dot, lot]
        ...
        
        DFS - dijkstra
        BFS - belman ford
        A * 
        Floyd Warshall 
        
        
        
        """
        
        
        """graph = {}
        
        wordList.append(beginWord)
        
        def compare(word1,word2):
            count = 0
            #print(word1)
            #print(word2)

            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1
            #print(count)
            return count == 1
                
        
        for i in range(0,len(wordList)-1):
            for j in range(i+1, len(wordList)):
                word1 ,word2 = wordList[i], wordList[j]
                if word1 != word2 and compare(word1,word2):
                    #print("HERE")
                    if word1 not in graph:
                        graph[word1] = []
                    graph[word1].append(word2)
                    if word2 not in graph:
                        graph[word2] = []
                    graph[word2].append(word1)
        

        q = collections.deque()
        #q[0]
        #q[-1]
        #q.pop()
        #q.popLeft()
        #q.append()
        q.append(beginWord)
        
        level = 1
        
        visited = set()
        visited.add(beginWord)
        
        #print(q)
        graph["word"] = ["w1","w2"]
        #print(graph)

        while q :
            
            for i in range(len(q)):
                
                word = q.popleft()
                #print(word)
                if word == endWord:
                    return level
                
                if word not in graph:
                    continue
                
                for w in graph[word]:
                    
                    if not w in visited:
                        q.append(w)
                        visited.add(w)

            level += 1
            
        return 0
        
        
        
        
        
        
        
        
        """
        
        
        """
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
        
        """
        
        if not endWord in wordList:
            return 0
        
        #graph = collections.defaultdict(list)

        graph = {}
        
        wordList.append(beginWord)
        
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                if pattern not in graph:
                    graph[pattern] = []
                graph[pattern].append(word)
        
        visited = set()
        visited.add(beginWord)
        
        q = collections.deque()
        #q[0]
        #q[-1]
        #q.pop()
        #q.popLeft()
        #q.append()
        q.append(beginWord)
        level = 1
        while q :
            
            for i in range(len(q)):
                
                word = q.popleft()
                #print(word)
                if word == endWord:
                    return level
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    
                    for w in graph[pattern]:
                        if not w in visited:
                            q.append(w)
                            visited.add(w)

            level += 1
            
        return 0
