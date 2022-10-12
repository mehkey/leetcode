class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.total = k
        self.q = Deque()

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q.append(value)
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.q.popleft()
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[0]
    
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[-1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.total


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()