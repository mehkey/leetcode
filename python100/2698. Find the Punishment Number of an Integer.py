class Solution:
    
    def maxUniqueSplit(self, s: str) -> int:
        
        def dfs(i, cnt):
            n = len(s)
            if i == n:
                if cnt == self.ii:
                    self.ans = True
                #ans = max(ans, cnt); 
                return 
            for j in range(i+1, n+1):    
                #if s[i:j] in visited: continue     
                #visited.add(s[i:j])               
                dfs(j, cnt+int(s[i:j]))             
                #visited.remove(s[i:j])             
        dfs(0, 0)                           
        return 
    
    def punishmentNumber(self, n: int) -> int:

        self.n = n
        
        s = 1
        
        '''
        def kwindow(L, k):
            for i in range(len(L)-k+1):
                yield L[i:i+k]


        def getAllWindows(L):
            for w in range(1, len(L)+1):
                yield from kwindow(L, w)

        def get_all_substrings(input_string):
            length = len(input_string)
            return [input_string[i:j+1] for i in range(length) for j in range(i,length)]

        '''
        for k in range(2, n+1):

            mul = k * k

            smul = str(mul)

            self.ii = k
            
            self.ans = False
            
            self.maxUniqueSplit(smul)
            
            if self.ans:
                s += k * k
            #for w in getAllWindows([c for c in smul]):
                #print(w)
                #if sum(w) == k:
                    #s += k * k
                #print(current)
            #L = mul
            #print(smul)
            #trust = safety
            #current = [int(L[i:i+j]) if L[i:i+j] != '' else 0 for i in range(0,len(L)) for j in range(1,len(L)-i+1)]

            #print(current)
            #for ss in current:
                #print(ss)
                #if sum(ss) == k:
                    #s += k * k
                    #break


            '''for j in range(1,len(smul)):
                #print(int(smul[0:j]) )
                #print(int(smul[j:]))
                #print('...')
                if int(smul[0:j]) + int(smul[j:]) == i:
                    #print("HERE")
                    s += i * i
                    break
            '''

        return s
