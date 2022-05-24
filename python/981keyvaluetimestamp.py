class TimeMap:

    def __init__(self):
        self.kvs = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        array = self.kvs.get(key,[]) 
        array.append([value,timestamp])
        self.kvs[key] = array

    def get(self, key: str, timestamp: int) -> str:

        #binarysearch
        array = self.kvs.get(key,[])

        #print(array)
        l = 0
        r = len(array)-1
        
        #minres = float("inf")
        minval = ""
        
        while(l <= r):

            mid = (l + r) //2

            if array[mid][1] <= timestamp:
                minval = array[mid][0]
                l  = mid + 1
            else:
                r = mid - 1

        return minval

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)