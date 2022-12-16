class Allocator:

    def __init__(self, n: int):
        self.arr = [None] * n
        self.last = 0
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        consec = 0
        
        for i in range(self.n) :#self.last):
            if self.arr[i] == None:
                if consec == 0:
                    consec+=1
                elif self.arr[i-1] == None:
                    consec+=1
            else:
                consec = 0
            
            if consec == size:
                self.fill(size,mID,i-size+1)
                return i-size+1
        '''
        if self.last + size <= self.n:
            self.fill(size,mID,self.last)
            ret = self.last
            self.last += size
            return ret
        else:
        '''
        return -1
    
    def fill(self, size: int, mID: int, start:int) -> int:

        for i in range(start, start+size):
            self.arr[i] = mID
        #print(self.arr)
        
    def free(self, mID: int) -> int:
        count = 0
        for i in range(self.n):  #self.last): #self.last
            if self.arr[i] == mID:
                self.arr[i] = None
                count+=1
        #print(self.arr)
        return count
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)