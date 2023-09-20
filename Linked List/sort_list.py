from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)
    
    def mergeSort(self, head):
        if head==None or head.next==None:
            return head

        mid = self.getMid(head)
        left_half = head
        right_half = mid.next
        mid.next = None
        left = self.mergeSort(left_half)
        right = self.mergeSort(right_half)

        merged_list = self.merge(left, right)
        return merged_list

    def merge(self, left, right):
        merged = ListNode(-1)
        curr = merged

        while left!=None and right!=None:
            if left.val<right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        if left:
            curr.next = left
        
        if right:
            curr.next = right
        
        return merged.next
    
    def getMid(self, head):
        slow = head
        fast = head

        while fast.next!=None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    

'''
Problem : https://leetcode.com/problems/sort-list/
TC : O(n log n)
SC : O(1) [O(log n) for call stack]
Approach :

1. Define the `sortList` function, which is the entry point for sorting the linked list. Call the `mergeSort` function on the `head` of the linked list and return the sorted result.

2. In the `mergeSort` function, check if the `head` is `None` or if it has only one element (base cases). If so, return the `head` as it is already sorted.

3. Find the middle of the linked list using the `getMid` function. Split the linked list into two halves: `left_half` and `right_half`.

4. Recursively call `mergeSort` on both `left_half` and `right_half`.

5. Merge the sorted `left` and `right` halves using the `merge` function. Create a dummy `merged` node to build the merged result.

6. Compare the values of the nodes from `left` and `right`, append the smaller node to the `merged` list, and advance the respective pointers.

7. After the loop, if there are any remaining nodes in `left` or `right`, append them to the `merged` list.

8. Return the `merged.next` node as the sorted linked list.

9. The `getMid` function uses two pointers, `slow` and `fast`, to find the middle of the linked list. `slow` moves one step at a time, while `fast` moves two steps at a time. When `fast` reaches the end of the list, `slow` will be at the middle.

'''