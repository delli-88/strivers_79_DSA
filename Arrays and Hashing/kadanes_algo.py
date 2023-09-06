from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_arr_sum = nums[0]
        max_till_now = nums[0]
        for i in range(1,len(nums)):
            max_till_now = max(nums[i],max_till_now+nums[i])
            max_sub_arr_sum = max(max_sub_arr_sum,max_till_now)
        return max_sub_arr_sum
        
print(Solution.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))

'''
Problem : https://leetcode.com/problems/maximum-subarray/
TC - O(n)
SC - O(1)

Approach :

1. Initialization:
   - Initialize two variables: `max_sub_arr_sum` and `max_till_now`, both set to the value of the first element in the `nums` list (`nums[0]`).
   - `max_sub_arr_sum` will store the maximum sum of a subarray encountered so far.
   - `max_till_now` will store the maximum sum ending at the current position (i.e., it keeps track of the current subarray being considered).

2. Iterate Through the List:
   - Start a loop from the second element of the `nums` list (index 1) and go up to the end of the list.
   - For each element at position `i`, calculate `max_till_now` as the maximum of two values:
     - The current element `nums[i]`.
     - The sum of the current element and the maximum sum ending at the previous position (`max_till_now + nums[i]`).
   - This step efficiently keeps track of the maximum sum ending at the current position.

3. Update `max_sub_arr_sum`:
   - In each iteration, update `max_sub_arr_sum` to be the maximum of two values:
     - The current `max_sub_arr_sum`.
     - The current `max_till_now`.
   - This step ensures that `max_sub_arr_sum` always holds the maximum sum of any subarray encountered during the loop.

4. Return Result:
   - After the loop completes, `max_sub_arr_sum` will contain the maximum sum of a contiguous subarray within the `nums` list.
   - Return `max_sub_arr_sum` as the final result.

This approach efficiently finds the maximum subarray sum by keeping track of the maximum sum ending at each position and updating the overall maximum accordingly. The time complexity of this algorithm is O(n), where n is the length of the input list `nums`.
'''