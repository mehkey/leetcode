class Solution:
    def partitionString(self, s: str) -> int:

        """
        m = set()

        count = 1

        for i,c in enumerate(s):

            if c in m:
                count += 1
            else:
                m.add(c)

        return count
        

        
        
        @cache
        def dfs(pos,count, prev):
            if pos >= len(s):
                return count

            c = (ord(s[pos]) - ord('a'))

            if c != prev:
                #arr[c] = 1
                return min(dfs(pos+1, count+1,  c ), dfs(pos+1, count,  c ))
            elif c == prev:
                return dfs(pos+1, count+1,  c )
            else:
                return dfs(pos+1, count+1,  c )
            
        arr = [0] * 26
        prev = -1
        return dfs(0,0,prev)
        
        

        nums[i] -= 1
        
       
        
        class Solution:
    def partitionString(self, s: str) -> int:

        def isUnique(s):
            return len(set(s)) == len(s)
			
		left = 0
        res = 0
        for right in range(1,len(s)+1):
            if not isUnique(s[left:right]):
                res += 1
                left = right-1
                
        return res+1 # don't forget there is still one partition we didn't add into res
        
        
        """
        
        m = set()

        count = 1

        for i,c in enumerate(s):

            if c in m:
                count += 1
            else:
                m.add(c)

        return count
        