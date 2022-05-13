# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        dummyNode = ListNode(0,None)
        
        dummyNode.next = head

        def findLast(node):
            for i in range(k-1):
                node = node.next
            return node
        
        last = findLast(dummyNode.next)
        
        previous = dummyNode
        current = head
        
        while last != None:
            #print(last.val)
            #print(current.val)
            #print("-------")
            
            temp2 = last.next

            while current.val != last.val :
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            
            #print(last.val)
            #print(current.val)
            #print("-------")
            
            current.next = temp2
            
            temp3 = last
            last = findLast(current.next)
            
            previous = temp3
            current = current.next
            #print(last.val)
            #print(current.val)
            #print(previous.val)
            #print("-------")

        return dummyNode.next