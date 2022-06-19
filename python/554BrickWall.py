class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        """
        
        1 2 2 1
        -__--_
        ---_--
        
        x
        
        -
        -
        -
        
        3
        
        [[1,2,2,1]
          [3,1,2]
         [1,3,2]
          [2,4]
         [3,1,2]
        [1,3,1,1]]
        
        0 cannot
        len(wall) cannot
        1,2,3,4,5... len(wall) - 1
        
        
        
        """
        
        """length = sum(wall[0])
        
        current = [0] * length
        
        #print(current)
        
        for row in range(len(wall)):

            for i in range(1,length): #1 to len(wall)-1
                current[i] = current[i] + 1

            total = 0
            for col in range(len(wall[row])-1):
                total += wall[row][col]
                #print(total)
                current[total] -= 1

        #print(current)
        #minCount = [float("inf"),0]
        
        #for val in range(1,len(current)) :
        #    minCount = minCount if minCount[0] < current[val] else [current[val],0]
        #    minCount[1] += 1
        #print(current)
        return min(current[1:]) if len(current) > 1 else len(wall)
        
        
        """
        
        """
        Use a hashmap to keep track of number of gaps
        
        """
        
        hm = {}
        
        for row in range(len(wall)):
            total = 0

            for gapindex in range(len(wall[row])-1):
                total += wall[row][gapindex]
                hm[total] = hm.get(total,0) + 1
        
        #print(hm)
        
        maximum= 0
        for key in hm:
            maximum = max(maximum, hm[key])
        
        return len(wall) - maximum
        