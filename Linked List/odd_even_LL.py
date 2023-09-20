from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head

'''
Problem : https://leetcode.com/problems/odd-even-linked-list/
TC : O(n)
SC : O(1)
Approach :

1. Check if the linked list is empty (head is None). If it is, return the empty list.

2. Initialize two pointers, `odd` and `even`, to the head of the linked list. Also, create a pointer `even_head` to keep track of the start of the even-indexed list.

3. Traverse the linked list using a while loop. In each iteration:
   - Update `odd.next` to point to the next odd-indexed node (i.e., `even.next`).
   - Move the `odd` pointer to the next odd-indexed node (i.e., `odd = odd.next`).
   - Update `even.next` to point to the next even-indexed node (i.e., `odd.next`).
   - Move the `even` pointer to the next even-indexed node (i.e., `even = even.next`).

4. After the loop, connect the last node of the odd-indexed list to the first node of the even-indexed list by setting `odd.next = even_head`.

5. Return the head of the modified linked list.

'''