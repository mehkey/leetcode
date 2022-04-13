class LRUCache:


    class LRUNode:
        key =0
        value =0
        previousNode = None 
        nextNode = None

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = self.next = None

    def __init__(self, capacity: int):
        self.first =  self.LRUNode(0,0)
        self.last =  self.LRUNode(0,0)
        self.first.nextNode = self.last
        self.last.previousNode = self.first
        self.capacity = capacity
        self.cache = {}
        self.total = 0

    def remove(self, node : LRUNode) -> None:
        #node = self.cache[key]
        #if node.previousNode :
            node.previousNode.nextNode = node.nextNode
        #if node.nextNode :
            node.nextNode.previousNode = node.previousNode
            #node.nextNode = node.Next
            #node.previous = 

    def insert(self, node : LRUNode) -> None:
        temp = self.first.nextNode
        self.first.nextNode = node
        node.nextNode = temp
        node.previousNode = self.first
        temp.previousNode = node



    def get(self, key: int) -> int:
        #print( "lenght is ", len(self.cache) )
        #print("get for ", key)

        if key in self.cache :
            #print("key in cache ", key)
            self.remove(self.cache[key])
            self.insert(self.cache[key]);

            return self.cache[key].value
        else:
            return -1


    def put(self, key: int, value: int) -> None:

        #print("put for", key)

        if key in self.cache :
            self.remove(self.cache[key])

        self.cache[key] = self.LRUNode(key,value)
        self.insert(self.cache[key])


        if len(self.cache) > self.capacity :
            
            la = self.last.previousNode
            #print("key is" , la.key)
            self.remove(la)
            del self.cache[la.key]

