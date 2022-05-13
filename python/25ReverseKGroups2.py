# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummyNode = ListNode(0,head)

        def findLast(node):
            for i in range(k-1):
                node = node.next
            return node

        groupPrevious = dummyNode

        while True:

            last = findLast(dummyNode.next)
            if not last:
                return dummyNode.next
        
            groupNext = last.next
            
            previous, current = last.next, groupPrevious.next
            
            while current.val != groupNext.val :
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            
            temp = groupPrevious.next
            groupPrevious.next= last
            groupPrevious = temp

        return dummyNode.next
    