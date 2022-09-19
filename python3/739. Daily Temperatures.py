class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        
        
        '''
        
        time:O(N^2) space:O(N) 
        for each start, find the grater temp
        
        
        O(N) O(N)
        
        decreasing data structure
        
        73
        
        74
        
        75
        
        75 71
        
        75 71 69
        
        75 72
        
        
        73,0
        
        74,1
        
        75,2
        
        75,2 71,3
        
        75,4 71,3 69,4
        
        75 72
        
        
        '''
        ans = [0] * len(T)
        s = []
        for i,t in enumerate(T):
            
            while s and s[-1][0] < t:
                old_t, old_ind = s.pop()
                ans[old_ind] = i - old_ind
            s.append((t,i))

        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        
        
        
        
        
        
        
        
        
        
        
        
        
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            #print(i, stack, ans)
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)

        return ans
        '''