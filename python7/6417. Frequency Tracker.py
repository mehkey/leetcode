class FrequencyTracker:

    def __init__(self):
        self.d = defaultdict(int)
        self.c = defaultdict(int)

    def add(self, number: int) -> None:
        self.c[self.d[number]] -= 1
        if not self.c[self.d[number]]:
            del self.c[self.d[number]]

        self.d[number] += 1
        self.c[self.d[number]] += 1
        
    def deleteOne(self, number: int) -> None:
        self.c[self.d[number]] -= 1
        if not self.c[self.d[number]]:
            del self.c[self.d[number]]

        if self.d[number] :
            self.d[number] -= 1
        
            self.c[self.d[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        
        return frequency in self.c
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)