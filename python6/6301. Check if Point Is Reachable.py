class Solution:
    def isReachable(self, x: int, y: int) -> bool:
        
        '''
        hm = {}
        
        v = set()
        
        @cache
        def dfs(x,y):
            
            print(x,y)
            #
            if (x,y) in v:
                return False
            
            v.add((x,y))
            
            if x <=0 or y <= 0:
                return False
            
            if x==targetX and y ==targetY:
                return True
            
            if x > targetX + y or x > 2*targetX:
                return False
            
            if y > targetY + x or y > 2*targetY:
                return False
            
            if dfs(x, y-x) or dfs(x-y, y) or dfs(2*x, y) or dfs(x, 2*y) :
                return True
            
            return False
            
            
        
        return dfs(1,1)
        '''
        
        while x%2==0 and y%2==0 :
            x//=2;
            y//=2;
        
        return gcd(x,y)==1
            
        