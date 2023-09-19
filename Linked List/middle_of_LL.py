# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        
        slow = head
        fast = head

        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
        
        return slow


'''
Problem : https://leetcode.com/problems/middle-of-the-linked-list/
TC : O(n)
SC : O(1)

Approach :

1. Initialize two pointers, `slow` and `fast`, to the head of the linked list.

2. Traverse the linked list with `fast` moving twice as fast as `slow`. This means that in each iteration, `slow` moves one step while `fast` moves two steps.

3. Continue this traversal until `fast` reaches the end of the linked list. At this point, `slow` will be at the middle node because it has moved half as many steps as `fast`.

4. Return the node pointed to by `slow` as the middle node.

'''