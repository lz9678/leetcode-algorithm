# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Nodes: 
1. Trick: When the two linked list intersect on a node M, all the nodes after this node M will be the same (same number of remaining nodes, and same value in each node). If we could make the nodes after M on two linked list match each other.
2. The underscore _ is used as a loop variable. It indicates that you are iterating a certain  number of times equal to the difference between len_l and len_s, but you don't intend to use the loop variable _ inside the loop body. 
'''
# Method 1: Using the trick
# Version 1
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # get the size of each linked list
        lenA = lenB = 0
        cur = headA
        while cur:
            cur = cur.next
            lenA += 1
        cur = headB
        while cur:
            cur = cur.next
            lenB += 1

        # let's match the two linked list
        cur_s, cur_l = headA, headB # initiate two pointers (assume A is shorter than B)
        len_s, len_l = lenA, lenB
        if lenA > lenB:
            cur_s, cur_l = cur_l, cur_s # swap the variable when A is actually longer than B
            len_s, len_l = len_l, len_s
        for _ in range(len_l - len_s):
            cur_l = cur_l.next # move the pointer of the long linkded list

        # compare the node in two linked list and find the intersection
        while cur_s:
            if cur_s == cur_l:
                return cur_s
            else:
                cur_l = cur_l.next
                cur_s = cur_s.next
        return None
    
    
# Version 2: Using the function to simplify
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # call the function to calculate the length
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        
        # call the function to move the pointer -- only work on the longer list
        if lenA > lenB:
            headA = self.moveForward(headA, lenA - lenB)
        else:
            headB = self.moveForward(headB, lenB - lenA)
        
        # get the intersection
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
    
    # create a function to calculate the linkded list length
    def getLength(self, head: ListNode) -> int: 
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    # create a function to move the pointer forward in a linked list
    def moveForward(self, head: ListNode, steps: int) -> ListNode:
        while steps > 0:
            head = head.next
            steps -= 1
        return head
    

# Version 3: Almost the same as the version 2
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        # match two linkede list 
        dis = self.getLength(headA) - self.getLength(headB)
        if dis > 0:
            headA = self.moveForward(headA, dis)
        else:
            headB = self.moveForward(headB, abs(dis))
        
        # get the intersection
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
    
    # Get length function
    def getLength(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    # Move forward function
    def moveForward(self, head: ListNode, steps: int) -> ListNode:
        while steps > 0:
            head = head.next
            steps -= 1
        return head
    
# Method 2: Don't understand this
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 处理边缘情况
        if not headA or not headB:
            return None
        
        # initiate two pointers
        pointerA = headA
        pointerB = headB
        
        # 遍历两个链表直到指针相交
        while pointerA != pointerB:
            # if the current node in list A is not null, we move to the next node, otherwise head of list B 
            pointerA = pointerA.next if pointerA else headB
            # if the current node in list B is not null, we move to the next node, otherwise head of list A 
            pointerB = pointerB.next if pointerB else headA
            
        
        # 如果相交，指针将位于交点节点，如果没有交点，值为None
        return pointerA