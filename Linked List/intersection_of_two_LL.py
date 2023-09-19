from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA==None and headB==None:
            return None

        ptr_a = headA
        ptr_b = headB

        while ptr_a!=ptr_b:
            ptr_a = ptr_a.next
            ptr_b = ptr_b.next
            if ptr_a==None:
                ptr_a = headB
            
            if ptr_b==None:
                ptr_b = headA

        return ptr_a
'''
Problem : https://leetcode.com/problems/intersection-of-two-linked-lists/
TC : O(2m)
SC : O(1)
Approach :

1. Initialize two pointers, `ptr_a` and `ptr_b`, to the heads of the linked lists `headA` and `headB`, respectively.

2. Traverse both linked lists simultaneously by moving `ptr_a` and `ptr_b` one node at a time.

3. When either `ptr_a` or `ptr_b` reaches the end of its respective linked list (i.e., becomes `None`), reassign it to the head of the other linked list. This ensures that both pointers have traveled the same distance when they meet.

4. Continue this process until `ptr_a` and `ptr_b` point to the same node. This node is the intersection point of the two linked lists.

5. Return the intersection node, which is now pointed to by both `ptr_a` and `ptr_b`.

'''

    # other sols
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # if headA==None and headB==None:
        #     return None
        # if headA.next==None and headB.next == None:
        #     if headA==headB:
        #         return headA
        #     return None
        # list_a_len = 0
        # list_b_len = 0
        # list_a_ptr = headA
        # list_b_ptr = headB

        # while list_a_ptr!=None:
        #     list_a_len+=1
        #     list_a_ptr = list_a_ptr.next

        # while list_b_ptr!=None:
        #     list_b_len+=1
        #     list_b_ptr = list_b_ptr.next

        # list_a_ptr = headA
        # list_b_ptr = headB
        # if list_a_len>list_b_len:
        #     to_travel = list_a_len - list_b_len
        #     for _ in range(to_travel):
        #         list_a_ptr = list_a_ptr.next
        # else:
        #     to_travel = list_b_len - list_a_len
        #     for _ in range(to_travel):
        #         list_b_ptr = list_b_ptr.next
        
        # while list_a_ptr!=None and list_a_ptr.next!=None:
        #     if list_a_ptr.next==list_b_ptr.next:
        #         return list_b_ptr.next
        #     list_a_ptr = list_a_ptr.next
        #     list_b_ptr = list_b_ptr.next
        # return None
    

