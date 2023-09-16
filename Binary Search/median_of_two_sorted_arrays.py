from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        if nums1_len>nums2_len:
            return self.findMedianSortedArrays(nums2, nums1)

        total_len = nums1_len+nums2_len
        start = 0
        end = nums1_len
        left_nums = (nums1_len + nums2_len + 1)//2
        while start<=end:
            mid1 = (start+end)//2
            mid2 = left_nums - mid1

            left1 = -float("inf")
            if mid1 -1 >=0:
                left1 = nums1[mid1-1]

            left2 = -float("inf")
            if mid2 -1 >=0:
                left2 = nums2[mid2-1]

            right1 = float("inf")
            if mid1<nums1_len:
                right1 = nums1[mid1]
            
            right2 = float("inf")
            if mid2<nums2_len:
                right2 = nums2[mid2]
            
            if left1>right2:
                end = mid1 - 1
            elif left2>right1:
                start = mid1 + 1
            else : # left1<=right2 and left2<=right1
                break
        
        is_odd_len = False
        if total_len%2!=0:
            is_odd_len = True

        if is_odd_len:
            return round(max(left1, left2), 5)
        else:
            return round(((max(left1, left2) + min(right1, right2))/2),5)

# print(Solution().findMedianSortedArrays(nums1 = [7,12,14,15], nums2 = [1,2,3,4,9,11]))
print(Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
'''
Problem : https://leetcode.com/problems/median-of-two-sorted-arrays/
TC : O(log min(nums1, nums2))
SC : O(1)
Approach :

1. Ensure that `arr1` is the smaller array, if not, swap the arrays to make `arr1` the smaller one.

2. Calculate the length of the left half: `left = (n1 + n2 + 1) // 2`, where `n1` is the length of `arr1` and `n2` is the length of `arr2`.

3. Initialize pointers `low` and `high` where `low = 0` and `high = n1` initially.

4. In a loop, calculate `mid1` and `mid2` as follows:
   - `mid1 = (low + high) // 2`
   - `mid2 = left - mid1`

5. Calculate `l1`, `l2`, `r1`, and `r2` using:
   - `l1 = arr1[mid1 - 1]` (or a default value if `mid1` is out of bounds)
   - `l2 = arr2[mid2 - 1]` (or a default value if `mid2` is out of bounds)
   - `r1 = arr1[mid1]` (or a default value if `mid1` is out of bounds)
   - `r2 = arr2[mid2]` (or a default value if `mid2` is out of bounds)

6. Check the following conditions to eliminate halves:
   - If `l1 <= r2 && l2 <= r1`, you've found the answer. break

7. If `l1 > r2`, eliminate the right half by setting `high = mid1 - 1`.
8. If `l2 > r1`, eliminate the left half by setting `low = mid1 + 1`.

9. If `(n1 + n2)` is odd, return `max(l1, l2)` as the median.
   - Otherwise, return `(max(l1, l2) + min(r1, r2)) / 2.0` as the median.
'''