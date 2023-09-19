from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next
        
        while fast.next!=None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next
    
'''
Problem : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
TC : O(n)
SC : O(1)
Approach :

1. Create a `dummy` node and set its `next` pointer to the `head` of the linked list. This dummy node helps to handle edge cases when removing the first node.

2. Initialize two pointers, `slow` and `fast`, to the `dummy` node.

3. Move the `fast` pointer `n` nodes ahead in the linked list. This creates a gap of `n+1` nodes between `slow` and `fast`.

4. Traverse the linked list while advancing both `slow` and `fast` one node at a time until `fast` reaches the end (i.e., `fast.next` becomes `None`). This ensures that `slow` will be pointing to the node just before the nth node from the end.

5. Update the `next` pointer of `slow` to skip the nth node, effectively removing it from the linked list.

6. Return the modified linked list, which is now the `next` node of the `dummy` node.

'''