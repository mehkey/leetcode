class Solution:
    def addMinimum(self, word: str) -> int:
        
        @cache
        def dp(i,cur):
            
            if i == len(word) and cur =='a':
                return 0
            if i == len(word) and cur =='b':
                return 2
            if i == len(word) and cur =='c':
                return 1
            
            if cur == 'a':
                if word[i] == 'a':
                    return dp(i+1,'b')
                if word[i] == 'b':
                    return dp(i,'b')+1
                if word[i] == 'c':
                    return dp(i,'c')+2

            if cur == 'b':
                if word[i] == 'b':
                    return dp(i+1,'c')
                if word[i] == 'a':
                    return dp(i,'a') +2
                if word[i] == 'c':
                    return dp(i,'c')+1

            if cur == 'c':
                if word[i] == 'c':
                    return dp(i+1,'a')
                if word[i] == 'a':
                    return dp(i,'a') +1
                if word[i] == 'b':
                    return dp(i,'b')+2
        
        
        return dp(0,'a')

def addMinimum(self, word: str) -> int:
        k, prev = 0, 'z'
        for c in word:
            k += c <= prev
            prev = c
        return k * 3 - len(word)


class Solution {
public:
    int addMinimum(string word) {
        
        int n = word.size(), i = 0, res = 0;
        
        while(i < n) {
            int count = 0;
            
            if(word[i] == 'a') {
                count++;i++;
            }
             
            if(i < n and word[i] == 'b') {
                count++;i++;
            }
            
            if(i < n and word[i] == 'c') {
                count++;i++;
            }
            
            res += 3 - count;
        }
        
        return res;
    }
};

class Solution:
    def addMinimum(self, word: str) -> int:
        n = len(word)
        i = 0
        res = 0
        
        while i < n:
            count = 0
            
            if word[i] == 'a':
                count += 1
                i += 1
             
            if i < n and word[i] == 'b':
                count += 1
                i += 1
            
            if i < n and word[i] == 'c':
                count += 1
                i += 1
            
            res += 3 - count
        
        return res