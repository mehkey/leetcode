class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        
        """

        hm # key is pair (a,b) -> 2
        hm # key is pair (b,a) -> 0.5

        hm # key is character value is a list 
        a -> b

        b -> a,c


        a -> z

        ...

        ab
        bc
        cd
        ce

        ac
        ad
        ae
        af

        ...

        bfs(first,last)


        """

        hashMapPairs = {}
        hashMapLinks = {}

        i = 0

        for equation in equations:
            X = equation[0]
            Y = equation[1]
            hashMapPairs[(X,Y)] = values[i]
            hashMapPairs[(Y,X)] = 1 / values[i]

            if not X in hashMapLinks:
                hashMapLinks[X] = []
            hashMapLinks[X].append(Y)

            if not Y in hashMapLinks:
                hashMapLinks[Y] = []
            hashMapLinks[Y].append(X)

            i += 1

        res = []

        for q in queries:

            visited = set()

            X, Y = q[0], q[1]
            #print(X, Y)

            if X not in hashMapLinks:
                res.append(-1.0)
                continue
                
            if X == Y:
                #print(res[-1])
                res.append(1.0)
                continue

            if (X,Y) in hashMapPairs:
                #print(res[-1])
                res.append(hashMapPairs[(X,Y)])
                continue

            hashMapPairs[(X,X)] = 1.0

            q = deque()
            q.append(X)

            cur = 1.0

            while q:

                C = q.popleft()

                visited.add(C)

                if C == Y:
                    if (X,C) in hashMapPairs:
                        res.append(hashMapPairs[(X,C)])
                        break
                    else:
                        res.append(-1.0)
                        break

                for N in hashMapLinks[C]: 
                    if N not in visited:
                        hashMapPairs[(X,N)] = hashMapPairs[(X,C)] * hashMapPairs[(C,N)]
                        hashMapPairs[(N,X)] = 1 / hashMapPairs[(X,N)]

                        q.append(N)
            
            else :
                res.append(-1.0)
            
            #print(res)

        #print(hashMapPairs)
        return res



        def calcEquation(self, equations, values, queries):
    quot = collections.defaultdict(dict)
    for (num, den), val in zip(equations, values):
        quot[num][num] = quot[den][den] = 1.0
        quot[num][den] = val
        quot[den][num] = 1 / val
    for k in quot:
        for i in quot[k]:
            for j in quot[k]:
                quot[i][j] = quot[i][k] * quot[k][j]
    return [quot[num].get(den, -1.0) for num, den in queries]



    class DJS:
    def __init__(self, alphabet):
        self.parent = {char: char for char in alphabet}
        self.vals = {char: 1.0 for char in alphabet}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x], val = self.find(self.parent[x])
            self.vals[x] *= val
        return self.parent[x], self.vals[x]
    
    def union(self, y, x, val):
        x, valx = self.find(x)
        y, valy = self.find(y)
        if x == y: return
        self.parent[y] = self.parent[x]
        self.vals[y] = val * valx / valy


__init__ end



class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        
        """

        hm # key is pair (a,b) -> 2
        hm # key is pair (b,a) -> 0.5

        hm # key is character value is a list 
        a -> b

        b -> a,c


        a -> z

        ...

        ab
        bc
        cd
        ce

        ac
        ad
        ae
        af

        ...

        bfs(first,last)


        

        hashMapPairs = {}
        hashMapLinks = {}

        i = 0

        for equation in equations:
            X = equation[0]
            Y = equation[1]
            hashMapPairs[(X,Y)] = values[i]
            hashMapPairs[(Y,X)] = 1 / values[i]

            if not X in hashMapLinks:
                hashMapLinks[X] = []
            hashMapLinks[X].append(Y)

            if not Y in hashMapLinks:
                hashMapLinks[Y] = []
            hashMapLinks[Y].append(X)

            i += 1

        res = []

        for q in queries:

            visited = set()

            X, Y = q[0], q[1]
            #print(X, Y)

            if X not in hashMapLinks:
                res.append(-1.0)
                continue
                
            if X == Y:
                #print(res[-1])
                res.append(1.0)
                continue

            if (X,Y) in hashMapPairs:
                #print(res[-1])
                res.append(hashMapPairs[(X,Y)])
                continue

            hashMapPairs[(X,X)] = 1.0

            q = deque()
            q.append(X)

            cur = 1.0

            while q:

                C = q.popleft()

                visited.add(C)

                if C == Y:
                    if (X,C) in hashMapPairs:
                        res.append(hashMapPairs[(X,C)])
                        break
                    else:
                        res.append(-1.0)
                        break

                for N in hashMapLinks[C]: 
                    if N not in visited:
                        hashMapPairs[(X,N)] = hashMapPairs[(X,C)] * hashMapPairs[(C,N)]
                        hashMapPairs[(N,X)] = 1 / hashMapPairs[(X,N)]

                        q.append(N)
            
            else :
                res.append(-1.0)
            
            #print(res)

        #print(hashMapPairs)
        return res
        
        """
        
        class DJS:
            def __init__(self, alphabet):
                self.parent = {char: char for char in alphabet}
                self.vals = {char: 1.0 for char in alphabet}

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x], val = self.find(self.parent[x])
                    self.vals[x] *= val
                return self.parent[x], self.vals[x]

            def union(self, y, x, val):
                x, valx = self.find(x)
                y, valy = self.find(y)
                if x == y: return
                self.parent[y] = self.parent[x]
                self.vals[y] = val * valx / valy

        alphabet = set(sum(equations, []))
        ufo = DJS(alphabet)
        for (y, x), val in zip(equations, values):
            ufo.union(y, x, val)

        res = []

        for y, x in queries:
            if x not in alphabet or y not in alphabet: 
                res.append(-1.0)
                continue
            y, valy = ufo.find(y)
            x, valx = ufo.find(x)
            if x == y: res.append(valy / valx)
            else: res.append(-1.0)
        return res