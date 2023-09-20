from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head

        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next

            if slow==fast:
                return True

        return False

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next

            if slow==fast:
                break

        if fast==None or fast.next==None:
            return None

        fast = head

        while slow!=fast:
            slow = slow.next
            fast = fast.next
        
        return slow



'''
hasCycle() -> checks if a LL has a cycle or not 
Problem : https://leetcode.com/problems/linked-list-cycle/
TC : O(n)
SC : O(1)
Approach :

1. Initialize two pointers, `slow` and `fast`, and set them both to the head of the linked list.

2. Use a while loop to traverse the linked list:
   - In each iteration, move the `slow` pointer one step ahead.
   - Move the `fast` pointer two steps ahead. (This simulates the "tortoise" and "hare" moving at different speeds.)

3. Check in each iteration if the `slow` and `fast` pointers meet (i.e., their references are the same). If they do meet, it indicates the presence of a cycle in the linked list.

4. If the `fast` pointer reaches the end of the linked list (i.e., `fast` or `fast.next` becomes `None`), it means there is no cycle, and you can return `False`.

5. If the `slow` and `fast` pointers meet during traversal, return `True` to indicate the presence of a cycle in the linked list.

This approach efficiently detects a cycle by using two pointers moving at different speeds. If there's a cycle, the fast pointer will eventually catch up to the slow pointer, confirming the cycle's existence. If there's no cycle, the fast pointer will reach the end of the list without meeting the slow pointer.

detectCycle() -> finds starting node of cycle
Problem : https://leetcode.com/problems/linked-list-cycle-ii/
TC : O(n)
SC : O(1)
Approach :

1. Initialize two pointers, `slow` and `fast`, to the head of the linked list.

2. Use a while loop to traverse the linked list:
   - In each iteration, move the `slow` pointer one step ahead.
   - Move the `fast` pointer two steps ahead.

3. Check in each iteration if the `slow` and `fast` pointers meet (i.e., their references are the same). If they do meet, it indicates the presence of a cycle in the linked list.

4. After breaking out of the loop (when `slow` and `fast` meet or `fast` reaches the end), check if `fast` is `None` or `fast.next` is `None`. If either condition is true, return `None` to indicate that there is no cycle.

5. If `fast` is not `None` and `fast.next` is not `None`, it means there is a cycle in the linked list. In this case, reset the `fast` pointer to the head of the linked list.

6. Use another while loop to find the node where the cycle starts:
   - In each iteration, move the `slow` pointer one step ahead.
   - Move the `fast` pointer one step ahead.
   - Continue this process until `slow` and `fast` meet again. When they meet, it indicates they have reached the starting node of the cycle.

7. Return either `slow` or `fast` as they now point to the starting node of the cycle in the linked list.

slow = fast
2(l1 + l2 + x1n) = l1 + l2 + x2n
l1 + l2 = n(x2-x1)= ny
l1 = ny - l2
l1 = n(y-1) + n -l2
l1 =  n(y-1) + d

so the distance of head to start node of linkedlist cycle = some n cycles of LL +
                                                    the distance/num nodes from colliding point to start of linkedlist cycle 

'''