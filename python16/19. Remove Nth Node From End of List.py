# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0

        cur = head
        while cur:
            cur = cur.next
            size += 1
        
        dum = ListNode(0,head)
        cur = dum

        while cur and size -n >= 1:
            cur = cur.next
            n += 1
        
        if cur and cur.next:
            cur.next = cur.next.next
        
        return dum.next
        

        
        
        
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next

        dummy = ListNode(0,head)

        cur = dummy

        for i in range(n+1):
            cur = cur.next

        if cur:
            if cur.next.next:
                cur.next = cur.next.next

        return head

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        size = 0

        cur = head
        while cur:
            cur = cur.next
            size += 1
        
        dum = ListNode(0,head)
        cur = dum

        while cur and size -n >= 1:
            cur = cur.next
            n += 1
        
        if cur and cur.next:
            cur.next = cur.next.next
        
        return dum.next
        
        