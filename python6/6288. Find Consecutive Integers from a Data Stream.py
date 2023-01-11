class DataStream:

    def __init__(self, value: int, k: int):
        self.total = 0
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:

        if num == self.value:
            self.total += 1
        
        else:
            self.total = 0

        return self.total >= self.k
            


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)