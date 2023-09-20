# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

''' Notes 
1. self: Refers to the instance of the ListNode class that's being created.
2. val: This is a parameter that you can pass when creating a new ListNode. It represents the value that the node will hold.
3. next: This is another parameter that represents the reference to the next node in the linked list. By default, it is set to None, indicating that this node doesn't point to any other node initially.
4. None in Python and NULL in SQL serve similar purposes as they both represent the absence of a value or an unknown value but with some differences.
'''

''' Two methods to remove element from linked list
1. For head node: move to the next node 
2. For non-head node: find the preivous node, make it directly point to the next node, skip this node
So there are two solutions for this problem
1. Evaluate if the node is head or not, and use the corresponding node removing methods
2. Add a dummy head node ahead of all the original notes. In this way, all the nodes including the original head nodes are considered as non-head nodes, and therefore we can use the same method to remove the nodes
'''

# Method 1: Directly remove elements from the list without using dummy head
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None and head.val == val:
            head = head.next
        
        current = head
        while current is not None and current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head
    
''' Notes
1. "Optional" indicates that a parameter or a return value can be of a specific type or None. Here it means, the input type of variable head could be either ListNode or None. It also means the value returned of this function could be ListNode or None
2. "head = ListNode(next = head)" is not needed. In test cases, the "head" input is already a linked list, so we don't need to self define a new linked list in the codes, which will lead to the errors.
3. Use "while" instead of "if" to evaluate if the head node is not none and equal to target value --> if the original head node satisfies the criteria, we will generate a new head node, which also needs evaluation, so we need a while loop instead of a one-time if.
4. When "while" evaluates multiple conditions, Python evaluated them from left to the right.
5. Use "current.next.val == val" instead of "current.val == val" --> skip the node with value equal to target (no changes to current)
'''
 
# Method 2: Create a dummy head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(next = head)

        current = dummy_head
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy_head.next

'''Notes
1. assign dummy_head to current instead of current.next --> we can skip the node that satisfies the criteria
2. return dummy_head.next instead of head --> head could be deleted already whild dummy_head.next is what we are really looking for
'''
