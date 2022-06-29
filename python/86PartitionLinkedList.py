# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        
        dummy1 = s1 =  ListNode(0)
        dummy2 = s2 = ListNode(0)
        
        cur = head
        
        while cur:
            print(cur.val)
            if cur.val < x:
                s1.next = cur
                s1 = s1.next

            else:
                s2.next = cur
                s2 = s2.next
            
            temp = cur
            cur = cur.next
            temp.next = None
        
        s1.next = dummy2.next
        return dummy1.next

        """
        
        dummy.next = head
        
        
        cur = head
        
        while cur:
            if cur.val == x:
                break
            cur = cur.next
        
        if not cur:
            return dummy.next

        p0 = dummy
        p1 = cur
        p2 = cur
        
        cur = head
        
        while cur:
            print(cur.val)
            print(p1.val)
            print(head)
            #print(p1.val)
            if cur.val < x:
                p0.next = cur
                cur = cur.next
                p0 = p0.next
                p0.next = None

            elif cur.val > x:
                p1.next = cur
                cur = cur.next
                p1 = p1.next
                p1.next = None

            else:
                cur = cur.next
        
        return dummy.next
        
        """