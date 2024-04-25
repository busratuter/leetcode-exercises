class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
    
        for _ in range(n + 1):
            second = second.next
        
        while second is not None:
            first = first.next
            second = second.next

        first.next = first.next.next
        
        return dummy.next
