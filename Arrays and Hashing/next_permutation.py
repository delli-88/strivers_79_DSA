from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        req_ind = -1
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                req_ind = i-1
                break
        
        if req_ind==-1:
            self.reverse(nums,0, len(nums)-1)
            return nums

        for i in range(len(nums)-1,req_ind,-1):
            if nums[i]>nums[req_ind]:
                nums[i], nums[req_ind] = nums[req_ind], nums[i]
                break
        self.reverse(nums, req_ind+1, len(nums)-1)

        return  nums
    
    def reverse(self, nums,start, end):
        while start<end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        return nums
    
print(Solution().nextPermutation(nums = [1,2,3]))

'''
Problem : https://leetcode.com/problems/next-permutation/
TC - O(n)
SC - O(1)

Approach:
1. Find the first decreasing element:
   - Initialize `req_ind` to -1.
   - Iterate through the `nums` list from right to left.
   - Compare each element `nums[i]` with its left neighbor `nums[i-1]`.
   - If `nums[i]` is greater than `nums[i-1]`, set `req_ind` to `i-1` and break out of the loop.

2. Check for no next permutation:
   - If `req_ind` remains -1 after the loop, it means there's no next permutation possible (the list is in descending order).
   - In this case, reverse the entire `nums` list.

3. Create the next permutation:
   - If `req_ind` is not -1 (indicating a decreasing element was found), proceed to create the next permutation.
   - Find the rightmost element in the list that is greater than `nums[req_ind]`.
   - Swap this rightmost element with `nums[req_ind]` to make the permutation lexicographically greater.
   - Reverse the portion of the list from `req_ind + 1` to the end to arrange the remaining elements in ascending order.

4. Return the modified `nums` list as the next permutation.
'''