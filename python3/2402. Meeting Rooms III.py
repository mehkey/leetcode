class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        total = [0] * n
        
        
        for m in meetings:
            
            while meeting > 0:
                
        
        
        return total.index(max(total))
        
        
        '''
        total = [0] * n
        
        s = [0] * n

        time = 0
        i = 0
        
        meetings.sort()
        
        while True:
            
            if min(s) == 0 and meetings[i][0] <= time:
                print('min(s)', min(s))
                print('time', time)
                print(time, meetings[i][0])
                
                for k in range(len(s)):
                    if s[k] == 0:
                        print(k)
                        s[k] = meetings[i][1] - meetings[i][0] + 1
                        total[k] += 1
                        i+=1
                        break
                print(s)

            if i == len(meetings):
                break

            for k in range(len(s)):
                if s[k] > 0:
                    s[k] -= 1

            time += 1
            
            
        print(total)
        
        m = max(total)
        
        for i in range(len(total)):
            if total[i] == m:
                return i
        
        '''
            