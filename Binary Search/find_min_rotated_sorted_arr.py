from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:

        start = 0
        end = len(nums)-1
        mini = float("inf")

        while start<=end:
            if nums[start]<=nums[end]:
                mini = min(mini, nums[start])
                break

            mid = (start+end)//2
            if nums[mid]>=nums[start]:
                mini = min(mini, nums[start])
                start = mid+1
            else:
                mini = min(mini, nums[mid])
                end = mid-1 
        return mini

print(Solution().findMin(nums = [3,1,2]))

'''
Problem : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
TC : O(log n)
SC : O(1)
Approach :

1. Initialize two pointers, `start` and `end`, to represent the current search range. Set `start` to 0 and `end` to the index of the last element in `nums`.

2. Initialize `mini` as positive infinity (`float("inf")`) to keep track of the minimum element.

3. Use a `while` loop to perform binary search within the search range:
   - Check if `nums[start]` is less than or equal to `nums[end]`. If true, it means the current subarray is already sorted. In this case, set `mini` to the minimum of `mini` and `nums[start]`, and break out of the loop because you've found the minimum element.

   - Calculate the middle index `mid` as `(start + end) // 2`.

   - If `nums[mid]` is greater than or equal to `nums[start]`, it means the left half of the array is sorted. In this case, set `mini` to the minimum of `mini` and `nums[start]`, and update `start` to `mid + 1` to search in the right half.

   - Otherwise, `nums[mid]` is less than `nums[start]`, indicating that the right half of the array is sorted. Set `mini` to the minimum of `mini` and `nums[mid]`, and update `end` to `mid - 1` to search in the left half.

4. After the `while` loop completes, return the value of `mini`, which represents the minimum element in the rotated sorted array.

'''