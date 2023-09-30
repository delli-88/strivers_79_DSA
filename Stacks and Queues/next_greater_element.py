from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [0]
        nums2_nge = {nums2[0]:-1}
        
        for i in range(1,len(nums2)):
            nums2_nge[nums2[i]] = -1
            while stack and nums2[stack[-1]]<nums2[i]:
                stack_top = stack.pop()
                nums2_nge[nums2[stack_top]] = nums2[i]
            stack.append(i)
        
        ans = []
        for i in range(len(nums1)):
            ans.append(nums2_nge[nums1[i]])

        return ans
    
    def nextGreaterElementCircular(self, nums):

        n = len(nums)
        stack = [0]
        nge_circular = [-1 for _ in range(n)]

        for i in range(1, 2*n):

            while stack and nums[stack[-1]]<nums[i%n]:
                stack_top = stack.pop()
                nge_circular[stack_top] = nums[i%n]
            stack.append(i%n)
        
        return nge_circular
print(Solution().nextGreaterElement([5,9,6,2],[2,3,1,9,7,6,5,8]))
    
print(Solution().nextGreaterElementCircular([2,3,1,9,7,6,5,8]))


'''

Approach :

Problem : https://leetcode.com/problems/next-greater-element-i
1. **Next Greater Element I (nextGreaterElement):**
   This function takes two lists, `nums1` and `nums2`, and returns a list of the next greater elements for each element in `nums1` from `nums2`.

   - Initialize an empty stack and a dictionary `nums2_nge` to store the next greater element for each element in `nums2`.
   - Iterate through `nums2` from left to right:
     - For each element, mark it as having no greater element (`-1`) in `nums2_nge`.
     - While the stack is not empty and the current element is greater than the element at the index stored in the stack's top, pop elements from the stack and update their next greater element to the current element.
     - Push the current element's index onto the stack.
   - Initialize an empty list `ans` to store the results.
   - Iterate through `nums1`:
     - For each element in `nums1`, append its next greater element from `nums2_nge` to the `ans` list.
   - Return the `ans` list as the result.
TC : O(m + n)
SC : O(n)

Problem : https://leetcode.com/problems/next-greater-element-ii/
2. **Next Greater Element II (nextGreaterElementCircular):**

   This function takes a list `nums`, which is a circular version of the "Next Greater Element I" problem, and returns a list of next greater elements for each element in `nums`.

   - Calculate the length `n` of the input list `nums`.
   - Initialize an empty stack and a list `nge_circular` to store the next greater element for each element in `nums`.
   - Iterate through `nums` twice (circularly):
     - While the stack is not empty and the current element is greater than the element at the index stored in the stack's top, pop elements from the stack and update their next greater element to the current element.
     - Push the current element's index modulo `n` onto the stack.
   - Return the `nge_circular` list as the result.
TC : O(n)
SC : O(n)
'''