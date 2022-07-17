class CircularQueue:
    def __init__(self, capacity):
        self.l = 0
        self.r = 0
        self.array = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def enqueue(self, val):

        if self.isFull():
            return False

        self.array[self.r] = val
        self.size += 1
        self.r += 1
        if self.r == self.capacity:
            self.r = 0

        return True

    def dequeue(self):

        if self.isEmpty():
            return False

        self.size -= 1
        self.l += 1
        if self.l ==  self.capacity:
            self.l = 0

        return True

    def front(self):
        return self.array[self.l] if not self.isEmpty() else -1

    def top(self):
        #print(self.r)
        return self.array[self.r - 1] if not self.isEmpty() else -1

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0




class MyCircularQueue:

    def __init__(self, k: int):
        self.nums = deque([])
        self.k = k

    def enQueue(self, value: int) -> bool:
        if len(self.nums) >= self.k:
            return False
        else:
            self.nums.append(value)
            return True

    def deQueue(self) -> bool:
        if not self.nums:
            return False
        else:
            self.nums.popleft()
            return True
            

    def Front(self) -> int:
        if not self.nums:
            return -1
        else:
            return self.nums[0]

    def Rear(self) -> int:
        if not self.nums:
            return -1
        else:
            return self.nums[-1]

    def isEmpty(self) -> bool:
        return not self.nums