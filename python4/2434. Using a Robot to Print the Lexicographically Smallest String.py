class Solution:

    def robotWithString(self, s: str) -> str:
        
        dic, t, ans = Counter(s), [], []
        for char in s:
            t.append(char)
            #print(t)
            if dic[char] == 1:
                del dic[char]
            else:
                dic[char] -= 1
            while dic and t and min(dic) >= t[-1]:
                ans += t.pop()
        ans += t[::-1]
        return ''.join(ans)
        
        
        
        '''
        #@cache
        @cache
        def dfs(s,t,p):
            
            if not s and not t:
                return p
            
            s1 = s2 = ''
            
            if s :
                s1 = dfs(s[1:],t + s[0], p )
            if t:
                s2 =  dfs(s,t[:-1], p + t[-1])
            
            if s1 and s2:
                if s1 < s2:
                    return s1
                else:
                    return s2
            else:
                if s1:
                    return s1
                if s2:
                    return s2

        return dfs(s,'','')
            
        
        res= ''
        
        l = 0
        r = len(s)-1
        
        while l <= r:
            #print(l,r)
            if l == r:
                res += s[r]
                l+=1
            elif s[l] < s[r]:
                res += s[l]
                #s = s[l+1:]
                l+=1
            elif s[l] > s[r]:
                res += s[r]
                #s = s[:r]
                r-=1
            else:
                res1 = self.robotWithString(s[:r])
                res2 = self.robotWithString(s[l+1:])
                if res1 < res2:
                    res += s[r]
                    #s = res1
                    r-=1
                else:
                    res += s[l]
                    #s = res2
                    l+=1
            
        return res
        
        '''
    
    

        
        
        dic, t, ans = Counter(s), [], []
        for char in s:
            t.append(char)
            #print(t)
            if dic[char] == 1:
                del dic[char]
            else:
                dic[char] -= 1
            while dic and t and min(dic) >= t[-1]:
                ans += t.pop()
        ans += t[::-1]
        return ''.join(ans)

        

        '''
        #@cache
        @cache
        def dfs(s,t,p):
            
            if not s and not t:
                return p
            
            s1 = s2 = ''
            
            if s :
                s1 = dfs(s[1:],t + s[0], p )
            if t:
                s2 =  dfs(s,t[:-1], p + t[-1])
            
            if s1 and s2:
                if s1 < s2:
                    return s1
                else:
                    return s2
            else:
                if s1:
                    return s1
                if s2:
                    return s2

        return dfs(s,'','')
            
        
        res= ''
        
        l = 0
        r = len(s)-1
        
        while l <= r:
            #print(l,r)
            if l == r:
                res += s[r]
                l+=1
            elif s[l] < s[r]:
                res += s[l]
                #s = s[l+1:]
                l+=1
            elif s[l] > s[r]:
                res += s[r]
                #s = s[:r]
                r-=1
            else:
                res1 = self.robotWithString(s[:r])
                res2 = self.robotWithString(s[l+1:])
                if res1 < res2:
                    res += s[r]
                    #s = res1
                    r-=1
                else:
                    res += s[l]
                    #s = res2
                    l+=1
            
        return res
        