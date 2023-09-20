# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Method 1: Two Pointers
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initiate a "current" node to loop through all the nodes, starting with "head"
        current = head
        # initiate another "pre" node
        pre = None
        while current: # when current is the none, the loop ends
            # change the "direction" of "current" node
            temp = current.next
            current.next = pre
            # move on to the next "current" node, and update "pre" node
            pre = current
            current = temp
        return pre
    
# Method 2: Recursion
# The thoughts behind this method is exactly the same as method 1 but with more simple codes
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # write a reverse function, and call it
        # set the initial value
        return self.reverse(head, None)
    
    def reverse(self, cur: ListNode, pre: ListNode) -> ListNode:
        # when will the reversion end? when the current is none
        if cur == None: 
            return pre
        # change the direction
        temp = cur.next
        cur.next = pre
        # change the initial value in the reverse function to move the pointer to the next node
        return self.reverse(temp, cur)