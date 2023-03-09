class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        '''
        if (time // n) % 2 ==0:
            
            return time % n + 1
        else:
            
            return n  - (time%n + 1)
        '''
        
        cur = 1
        
        f = True
        for i in range(time):
            
            if f:
                cur += 1
            else:
                cur -= 1
            
            if cur == 0:
                cur = 2
                f = True
            elif cur == n + 1:
                cur = n - 1
                f = False
        
        return cur
            
    
    int rounds = time/(n-1);
        int ans = 0;
        if(rounds%2 == 0){
            ans = (1+time%(n-1));
        }else{
            ans = (n-time%(n-1));
        }
        
        return ans;