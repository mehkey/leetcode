class Solution:

        def __init__(self, n: int, blacklist: List[int]):
        self.sz =n-len(blacklist)
        self.mapping = {i:666 for i in blacklist}
        self.black_list = blacklist
        self.last=n-1
        
        for i in blacklist:
            if  i>=self.sz: #needn't map if i in [sz,N)
                continue
            
            while self.last in self.mapping:   #needn't map if i in [sz,N)
                self.last-=1
            
            self.mapping[i]=self.last
            self.last-=1
            
    def pick(self) -> int:
        picked=random.randrange(self.sz)
        if picked in self.mapping:
            return self.mapping[picked]  #return original index
        return picked


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()