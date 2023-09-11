from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums)-1

        while start<=end:
            mid = (start+end)//2

            if nums[mid]==target:
                return True
            
            # duplicate at start, mid, end
            if nums[mid]==nums[start]==nums[end]:
                start+=1
                end-=1
            else:
                # left is sorted
                if nums[mid]>=nums[start]:
                    # target is in left
                    if target>=nums[start] and target<nums[mid]:
                        end = mid-1
                    else:
                        start = mid+1
                # right is sorted
                else:
                    # target is in right
                    if target>nums[mid] and target<=nums[end]:
                        start = mid+1
                    else:
                        end = mid - 1
        return False

print(Solution().search(nums = [4,5,6,6,7,0,1,2,4,4], target = 1))

'''
Problem : https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
TC : Θ(log n), O(n)
SC : O(1)
Approach : 

1. Initialize two pointers, `start` and `end`, to represent the current search range. Set `start` to 0 and `end` to the index of the last element in `nums`.

2. Use a `while` loop to perform binary search within the search range:
   - Calculate the middle index `mid` as `(start + end) // 2`.

   - Check if `nums[mid]` is equal to the `target`. If it is, return `True` because the target element is found.

   - Handle the case when there are duplicates at `start`, `mid`, and `end`:
     - Increment `start` by 1.
     - Decrement `end` by 1.

   - If the left half of the array is sorted (i.e., `nums[mid] >= nums[start]`):
     - Check if the `target` is within the left half (between `nums[start]` and `nums[mid]`):
       - If yes, update `end` to `mid - 1` to search in the left half.
       - If no, update `start` to `mid + 1` to search in the right half.

   - If the right half of the array is sorted (i.e., `nums[mid] < nums[start]`):
     - Check if the `target` is within the right half (between `nums[mid]` and `nums[end]`):
       - If yes, update `start` to `mid + 1` to search in the right half.
       - If no, update `end` to `mid - 1` to search in the left half.

3. If the `while` loop completes without finding the `target`, return `False` because the element is not in the array.
'''