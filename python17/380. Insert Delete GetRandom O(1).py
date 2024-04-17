class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.hm = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.hm:
            return False

        self.arr.append(val)
        self.hm[val] = len(self.arr) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.hm:
            return False

        ind = self.hm[val]
        
        self.hm[self.arr[-1]] = ind

        self.arr[ind], self.arr[-1] = self.arr[-1], self.arr[ind]

        self.arr.pop()

        del self.hm[val]

        return True

    def getRandom(self) -> int:
        ind = randint(0, len(self.arr) - 1)

        return self.arr[ind]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
