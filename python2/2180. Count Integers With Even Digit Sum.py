class Solution:
    def countEven(self, num: int) -> int:
        c = 0
        for i in range(1,num+1):
            #print([int(j) for j in str(i)])
            if sum([int(j) for j in str(i)]) % 2 ==0:
                c+=1
        
        return c