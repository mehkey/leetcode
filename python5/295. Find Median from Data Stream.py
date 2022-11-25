from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.s = SortedList()

    def addNum(self, num: int) -> None:
        self.s.add(num)

    def findMedian(self) -> float:
        l = len(self.s)
        if l%2==0:
            return (self.s[l//2-1]+self.s[l//2])/2
        return self.s[l//2]




class MedianFinder:

    def __init__(self):
        ### max heap to store the first half of the list
        self.maxHeap = []
        ### min heap to store the second half of the list
        self.minHeap = []

    def addNum(self, num: int) -> None:
        ### push num into the correct heap
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
        
        ### banance the two heaps so that each of them representing half of the list
        ### for odd length list, len(maxHeap) == len(minHeap)+1
        ### for even length list, len(maxHeap) == len(minHeap)
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap)) 
        elif len(self.maxHeap) > len(self.minHeap)+1:
            heappush(self.minHeap, -heappop(self.maxHeap)) 

    def findMedian(self) -> float:
        
        ### if the length of entire list is even, 
        ### get the mean of the two middle values
        if (len(self.maxHeap)+len(self.minHeap))%2==0:
            return (-self.maxHeap[0]+self.minHeap[0])/2
        
        ### when odd, we know that the median is in maxHeap
        return -self.maxHeap[0]