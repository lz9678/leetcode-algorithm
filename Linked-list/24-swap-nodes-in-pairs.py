# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Method 1: 
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # need to review why dummy_head is needed from previous questions
        # to swap the pair, we will always need the participation of three nodes: pre, cur, next
        dummy_head = ListNode(next=head)
        current = dummy_head
        # no need to initiate a temp variabel here, can directly use it in the loop
        # temp = None

        # you should put current.next ahead of current.next.next to avoid "empty pointer" error
        while current.next and current.next.next:
            temp = current.next
            # I missed the line below in my initial solution
            temp1 = current.next.next.next 

            # we will need both temp and temp1 before this line is executed
            current.next = current.next.next 
            current.next.next = temp
            temp.next = temp1

            # move to the next
            current = current.next.next

        # in my version, i did not use dummy_head, in the end, find it difficult to return to new head
        return dummy_head.next


# Method 2: Recursion
# The thought behind this is simliar to method 1 but slightly different
# Instead of using the previous node before the pair, we are using the next node after the pair
# This next node is also the result of the swap of the next pair which is where the recursion comes to play
# Pay attention to "return cur" in this solution
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # when will the recusion end? when the two nodes swapped is none
        if head is None or head.next is None:
            return head

        # pre and cur are the two nodes to swap
        pre = head
        cur = head.next
        next = head.next.next
        
        # swap the nodes
        cur.next = pre 
        pre.next = self.swapPairs(next) # key step
         
        return cur

