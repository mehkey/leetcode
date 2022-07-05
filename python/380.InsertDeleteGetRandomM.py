class RandomizedSet:

    
    """
    
    Insert -> id O(1)
    
    
    Insert to both (HM)
    
    
    Remove -> id O(1)
    
    
    Remove from both
    
    
    Random -> O(1) ->. range 0 -> n (total numbers)
    
    get from Array
    
    Array + HM
    
    
    HM : id -> pos in array
    
    Array : id
    
    Remove ()

    """
    def __init__(self):

        self.hm = defaultdict(int)
        self.a = []

    def insert(self, val: int) -> bool:
        #print(self.hm)
        #print(self.a)
        if val in self.hm :
            return False

        pos = len(self.a)
        
        self.a.append(val)
        
        self.hm[val] = pos

        return True


    def remove(self, val: int) -> bool:
        #print(self.hm)
        #print(self.a)
        if not val in self.hm :
            return False
        
        if len(self.a) == 1:
            del self.hm[val] #
            self.a.pop() #
            return True
        
        
        cur =  self.hm[val]
        
        new = self.a[len(self.a)-1]
        
        self.a[cur] = new
        
        self.a.pop()
        
        self.hm[new] = cur
        
        del self.hm[val]
        
        return True

    def getRandom(self) -> int:
        #print(self.hm)
        #print(self.a)
        if len(self.a) ==0:
            return -1

        i = random.randint(0,len(self.a)-1)
        return self.a[i]
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


class RandomizedSet:

    
    """
    
    Insert -> id O(1)
    
    
    Insert to both (HM)
    
    
    Remove -> id O(1)
    
    
    Remove from both
    
    
    Random -> O(1) ->. range 0 -> n (total numbers)
    
    get from Array
    
    Array + HM
    
    
    HM : id -> pos in array
    
    Array : id
    
    Remove ()

    """
    def __init__(self):

        self.hm = defaultdict(int)
        self.a = []

    def insert(self, val: int) -> bool:
        #print(self.hm)
        #print(self.a)
        if val in self.hm :
            return False

        pos = len(self.a)
        
        self.a.append(val)
        
        self.hm[val] = pos

        return True


    def remove(self, val: int) -> bool:
        #print(self.hm)
        #print(self.a)
        if not val in self.hm :
            return False
        
        cur =  self.hm[val]
        
        new = self.a[-1]
        
        self.a[cur] = new
        
        self.a.pop()
        
        self.hm[new] = cur
        
        self.hm.pop(val)
        
        return True

    def getRandom(self) -> int:
        #print(self.hm)
        #print(self.a)
        if len(self.a) ==0:
            return -1

        i = random.randint(0,len(self.a)-1)
        return self.a[i]
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()