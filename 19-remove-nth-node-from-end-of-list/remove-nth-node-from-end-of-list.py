class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        
        fast = slow = dummy
        
        # Move fast n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both pointers
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node
        slow.next = slow.next.next
        
        return dummy.next