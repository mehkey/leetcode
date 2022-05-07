# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None
        
        if not head.next:
            return head
        
        if k == 0:
            return head

        lastNode = head
        
        count = 1
        
        while lastNode.next :
            lastNode = lastNode.next
            count += 1
        
        if ( k % count) == 0:
            return head
        
        total = count
        cut = total - ( k % count)
        count = 0
        pointer = head 
        while count < cut - 1 :
            pointer = pointer.next
            count += 1
        
        temp = head
        
        head = pointer.next
        
        pointer.next = None
        
        lastNode.next = temp
        
        
        
        return head

        