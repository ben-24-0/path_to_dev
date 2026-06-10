class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        if slow is None:
            return False
        fast = slow.next

        while fast != slow and fast is not None:
            if fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next

        if fast == slow:
            return True
        return False