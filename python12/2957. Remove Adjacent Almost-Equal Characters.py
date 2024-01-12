class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        
        '''n = len(word)
        alf = 'abcdefghijklmnopqrstuvwxyz'
        #print(ord(word[0]))
        @cache
        def dp(i,cur,cur2):
            if i == n-1:
                return 0
            
            if cur == cur2 or abs(ord(cur) - ord(cur2)) == 1:
                #print(ord(cur) - ord('a')+2)
                nc = chr(ord(cur) - ord('a')+2)
                nc2 = chr(ord(cur2) - ord('a')+2)
                return min(dp(i,nc,cur2) + 1 , dp(i+1,cur,nc2) + 1)
            
            return dp(i+1,word[i+1],word[i+2])
        
        return dp(0,word[0],word[1])
        '''
        res = 0
        i = 0
        while i < len(word)-1:
            if word[i] == word[i+1] or abs(ord(word[i]) - ord(word[i+1])) == 1:
                res += 1
                i+=2
                continue
            i+=1
                
                
        return res