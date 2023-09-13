from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0

        if nums[0]>nums[1]:
            return 0
        
        if nums[-1]>nums[-2]:
            return len(nums)-1
        
        start = 1
        end = len(nums)-2

        while start<=end:
            mid = (start+end)//2

            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid

            if nums[mid]<nums[mid+1]:
                start = mid+1
            else:
                end = mid-1
        
        return -1


print(Solution().findPeakElement(nums = [1,2]))


'''
Problem : https://leetcode.com/problems/find-peak-element/ 
TC : O(logn)
SC : O(1)

Approach:
1. Check if the length of `nums` is 1. If it is, return 0 because the single element is a peak (no adjacent elements to compare).

2. Check if the first element, `nums[0]`, is greater than the second element, `nums[1]`. If true, return 0 because the first element is a peak.

3. Check if the last element, `nums[-1]`, is greater than the second-to-last element, `nums[-2]`. If true, return the index of the last element (i.e., `len(nums) - 1`) because the last element is a peak.

4. Initialize two pointers, `start` and `end`, to represent the current search range. Set `start` to 1 (index of the second element), and set `end` to `len(nums) - 2` (excluding the first and last elements).

5. Use a `while` loop to perform binary search within the search range:
   - Calculate the middle index `mid` as `(start + end) // 2`.

   - Check if `nums[mid]` is greater than both its adjacent elements (`nums[mid-1]` and `nums[mid+1]`). If true, return `mid` because `nums[mid]` is a peak.

   - If `nums[mid]` is less than `nums[mid+1]`, it indicates that the peak is on the right side. Update `start` to `mid + 1` to search in the right half.

   - Otherwise, update `end` to `mid - 1` to search in the left half.

6. If the `while` loop completes without finding a peak, return -1 to indicate that no peak element exists in the array.

'''