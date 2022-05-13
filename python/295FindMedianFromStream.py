class MedianFinder:

    

    def __init__(self):
        self.lowHeap = []
        self.highHeap = []


    def addNum(self, num: int) -> None:
        high = self.lowHeap[0] if len(self.lowHeap) > 0  else math.inf
        low = -self.highHeap[0] if len(self.highHeap) > 0  else -math.inf
        
        if num <= high:
            pop = heapq.heappop(self.lowHeap) if len(self.lowHeap) > 0 else 0
            heapq.heappush(self.lowHeap, - pop)

        elif num >= low:
            pop =  heapq.heappop(self.highHeap) if len(self.highHeap) else 0
            
            heapq.heappush(self.lowHeap, -pop)
        else:
            heapq.heapPush(self.lowHeap, num)
        
    def findMedian(self) -> float:
        
        high = self.lowHeap[0] if len(self.lowHeap) > 0 else 0
        low = -self.highHeap[0] if len(self.highHeap) > 0 else 0
        
        if len(self.lowHeap) == len(self.lowHeap) :
            return (low + high ) / 2
        else:
            return low



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()