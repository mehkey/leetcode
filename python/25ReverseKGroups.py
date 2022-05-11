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
            print(last.val)
            
            temp2 = last.next

            while current.val != last.val :
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            
            current.next = temp2

            last = findLast(current.next)
            
            previous = last
            current = last.next

        return dummyNode.next