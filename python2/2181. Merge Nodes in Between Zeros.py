# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        dummy = ListNode(-1)
        
        dummyNext = dummy
        
        cur = head
        
        s = 0
        while cur:
            if cur.val==0:
                
                if s != 0:
                    dummyNext.next = ListNode(s)
                    dummyNext = dummyNext.next
                    s = 0
            else:
                s += cur.val

            cur = cur.next
            

        return dummy.next