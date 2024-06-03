class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        N = len(words)
        
        def isp(s1,s2):
            if len(s1) > len(s2):
                return False
            
            #print(s2[:len(s1)], s2[len(s2) - len(s1):] )
            if s1 == s2[:len(s1)] and s1 == s2[len(s2) - len(s1):] :
                return True
            
            return False
        
        res = 0
        for i in range(N):
            for j in range(i+1,N):
                if isp(words[i],words[j]) :
                    #print(words[i],words[j])
                    res += 1
        
        return res