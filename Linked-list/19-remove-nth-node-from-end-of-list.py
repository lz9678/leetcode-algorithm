# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Method 1: Fast and slow pointer
''' Trick: 
1. Let fast pointer be quicker than slow one by n nodes, so when the fast pointer is pointing to the end (none), the slow pointer is pointing to what we want (the one to delete)
2. To make it easier to delete, we could let slow pointer pointing to the node right before the to-delete one, and therefore we should let fast pointer running faster than the slow one by n+1 nodes
'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:           
        # use dummy_head to simplify the problem
        # create two pointers with initial value assigned
        dummy_head = ListNode(val = 0, next = head)
        slow = fast = dummy_head
        
        # let fast run (n+1) nodes faster than the slow
        for i in range(n+1):
            fast = fast.next
        
        # move fast and slow at the same time until fast becomes "None"
        while fast:
            slow = slow.next
            fast = fast.next
        
        # delete the node by let slow directly pointing to the next next, skipping the deleted one
        slow.next = slow.next.next
        
        return dummy_head.next
