# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Trick: 
Assume we have two pointers, one is moving faster than the another one (fast vs. slow, move 2 steps each time vs. move only 1 step): 
If there is no cycle in the linked list, aka. the linked list is a straight line, then it is not possible for the two pointers to meet each other, since the fast one will always reach the end (None) quicker than the slow one.
However, if there is a cycle, then the two pointers will definitely meet each other!
Is it possible that the fast pointer keep chasing the slow one in the cycle but they never meet?
Possible! This happens when the fast pointer is two nodes faster than the slow one. In this way, whenever the fast one approaches the slow one, the fast might directly skip the slow one without cathing it. So we could assume the fast pointer moves 2 nodes per time, and slow one moves 1 node per time. In this way, fast pointer is actually chasing the slow one with speed at 1 node per time, therefore fast pointer would definitely be able to catch slow one in the end.
'''

'''
Method 1:
Assume the fast travels at speed 2 and slow travels at speed 1
travel distance of fast = x + y + n(z + y)
travel distanct of slow = x + y
[x + y + n(z + y)]/2 = (x+y)/1
x = n(y+z) - y
In this equation, n>=1 which means before fast meets slow, it should travel for at least one full cycle
can n be zero? No. A quick math, if n is zero, this equation would become x = -y which is not valid
x = (n-1)(y+z)+z *** a very important equation!
when n=1, x=z
when n=100, x = 99(y+z)+z (it is still x = z but with additional cycles --> draw the graph to understand)
why won't slow travel as = x + y + k(z+y) like quick (travel more than one cycle?)
because fast would catch slow before slow travels a full cycle
'''

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Define two pointers - slow and fast
        slow = head
        fast = head
        
        # Find the intersection of two pointers
        # since fast moves at two nodes, we need to make sure both fast and fast.next it not null
        # why don't we need to set the fast.next.next to be not null also? 
        # when fast.next.next is none, it is still okay only when fast.next is not null
        while fast and fast.next: 
            slow = slow.next # slow moves at one node
            fast = fast.next.next # fast moves at two nodes
            
            # this means when two pointers meet (if there is a cycle, they would definitely meet)
            if slow == fast:
                # define two new pointers to find the cycle entry using x = z equation
                index1 = fast # the intersection
                index2 = head # the head
                # since x = z, these two new pointers would meet at the cycle entry
                # use this loop to find their new meetup point aka the entry
                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
                return index1
        
        # If there is no cycle, the list is a straight line, the fast.next would be null eventually
        # In this case, the loop would end without returning anything, so æwe return null
        return None

# Method 2: Using set, very easy to understand 

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # initiate a set to contain nodes visited
        visited = set()
        
        # loop the linked list from the head node
        # if there is a cycle, the head here would never be None
        # we can only break the loop in the if condition
        # if there is no cycle, the if condition would never be triggered
        # when all the nodes are visited, the head would become None, and the loop stops
        while head:
            if head in visited:
                # entry node of the cycle would be the first ever node that being looped more than once
                return head
            # document all the visited node in the set, and then move on to the next node
            visited.add(head)
            head = head.next
        
        return None
