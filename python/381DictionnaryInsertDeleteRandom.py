class RandomizedCollection:

    def __init__(self):

        self.hm = defaultdict(tuple) # (id,occur)
        self.a = []

    def insert(self, val: int) -> bool:
        #print(self.hm)
        #print(self.a)
        if val in self.hm :
            t = self.hm[val]
            self.hm[val] = (t[0],t[1]+1)
            return False

        pos = len(self.a)
        
        self.a.append(val)
        
        self.hm[val] = (pos,1)

        return True


    def remove(self, val: int) -> bool:
        #print(self.hm)
        #print(self.a)
        if not val in self.hm :
            return False
        
        cur,ocur =  self.hm[val]
        
        if ocur == 1:
            
            new = self.a[-1]

            self.a[cur] = new

            self.a.pop()

            self.hm[new] = (cur,self.hm[new][1])

            self.hm.pop(val)
        elif ocur > 1:
            t = self.hm[val]
            self.hm[val] = (t[0],t[1]-1)
        else:
            raise Exception("Invalid state ... ")

        return True

    def getRandom(self) -> int:
        #print(self.hm)
        #print(self.a)
        if len(self.a) ==0:
            return -1

        i = random.randint(0,len(self.a)-1)
        return self.a[i]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()