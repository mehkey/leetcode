# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node = head
        
        arr = Deque()
        
        while node:
            while arr and arr[-1] < node.val:
                arr.pop()
            
            arr.append(node.val)

            node = node.next
        
        node = ListNode(0,None)
        head = node
        
        for val in arr:
            node.next = ListNode(val,None)
            node = node.next
        
        return head.next

            
        