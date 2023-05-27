class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        
        '''
        left = min(s, t)
        
        right = min(s, t)
        
        other = min(s, t)
        '''
        
        def checkforSubsequence(target, S):
 
            # Declare a stack
            ss = []

            # Push the characters of
            # target into the stack
            for i in range(len(target)):
                ss.append(target[i])

            # Traverse the string S in reverse
            for i in range(len(S) - 1, -1, -1):

                # If the stack is empty
                if (len(ss) == 0):
                    return True

                # If S[i] is same as the
                # top of the stack
                if (S[i] == ss[-1]):

                    # Pop the top of stack
                    ss.pop()

            # Stack s is empty
            if (len(ss) == 0):
                return True
            else:
                return False

        def is_subsequence(needle, haystack):
            current_pos = 0
            for c in needle:
                current_pos = haystack.find(c, current_pos) + 1
                if current_pos == 0:
                    return False
            return True

        
        def is_subseq(x, y):
            it = iter(y)
            return all(any(c == ch for c in it) for ch in x)
        
        @cache
        def isSubsequence(s, t):
            s, t = map(list, [s, t])
            for c in t:
                if c in s:
                    s.pop(0)
            return not s
    
        l = 0
        
        m = float('inf')
        
        if is_subsequence(t,s):
            return 0
        
        for i,r in enumerate(t):
            #while r in c:
            
            #cur = t[l:i+1] 
            
            cur = t[0:l] + t[i+1:]
            #print('TEST')
            #print(cur)
            #cur += t[i+1:] 
            #print(cur)
            
            #if l < i and is_subseq(cur,s):
                
            #    print('HERE', i - l + 1 )
            #    m = min(m, i - l + 1)
                
            #     l+=1
            #    cur = t[0:l] + t[i+1:]
                
            while l <= i and is_subsequence(cur,s):
                #print('HERE', i - l + 1 )
                #print(cur)
                m = min(m, i - l + 1)

                l+=1
                cur = t[0:l] + t[i+1:]
                #print(cur)
                
                #m = min()
                
                #print('HERE',i - l + 1 )
                #m = min(m, i - l + 1)

                '''
                l += 1
                #cur = t[0:l] + t[i:]
                cur = t[l:i+1] 
                print(cur)
            
                #print('HERE',i - l + 1 )
                m = min(m, i - l + 1)
                '''

        return m



class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        suffix = [-1]*len(s)
        j = len(t)-1
        for i in reversed(range(len(s))): 
            if 0 <= j and s[i] == t[j]: j -= 1
            suffix[i] = j 
        ans = j + 1
        j = 0 
        for i, ch in enumerate(s): 
            ans = min(ans, max(0, suffix[i] - j + 1))
            if j < len(t) and s[i] == t[j]: j += 1
        return min(ans, len(t)-j)