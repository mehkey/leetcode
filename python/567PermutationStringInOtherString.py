class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s = len(s1)
        
        window = [0] * 26
        
        goal = [0] * 26
        
        for i in range(0,len(s2)):
              
            if i < s :
                
                window[ord(s2[i]) - ord('a')] += 1
                goal[ord(s1[i])- ord('a')] += 1
            else:
                window[ord(s2[i])- ord('a')] += 1
                window[ord(s2[i-s])- ord('a')] -= 1
                #if i == 3: #s2[i] == 'a':
                    #print(window)
                    #print(goal)
                    #print(i)
            if sum(goal) == s and window == goal:
                return True

        
        return False

                