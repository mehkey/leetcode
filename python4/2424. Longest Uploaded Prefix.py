class LUPrefix:

    def __init__(self, n: int):
        self.s = set()
        self.max = n
        self.cur = 0

    def upload(self, video: int) -> None:
        
        
        if len(self.s) == self.max:
            return
        
        if self.cur == self.max:
            return
        
        self.s.add(video)
        
        c = self.cur + 1
        
        while c in self.s:
            self.cur = c
            c = c + 1

    def longest(self) -> int:
        return self.cur


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()