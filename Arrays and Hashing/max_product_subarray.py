from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = -float("inf")
        prefix = 1
        suffix = 1
        for i in range(n):
            if prefix==0:
                prefix = 1
            if suffix==0:
                suffix=1
            prefix = prefix*nums[i]
            suffix = suffix*nums[n-i-1]
            maxi = max(maxi, prefix, suffix)
        return maxi

print(Solution().maxProduct(nums = [2,3,0,4,6]))

'''
Problem : https://leetcode.com/problems/maximum-product-subarray/
TC : O(n)
SC : O(1)
Approach :

1. Initialize variables:
   - `maxi` to track the maximum product (initialized as negative infinity).
   - `prefix` and `suffix` to maintain products from the start and end of the array (initialized as 1).

2. Iterate through the elements of `nums` using a `for` loop:
   - If `prefix` becomes zero, reset it to 1 to avoid affecting the product.
   - If `suffix` becomes zero, reset it to 1 to avoid affecting the product.
   - Update `prefix` by multiplying it with the current element.
   - Update `suffix` by multiplying it with the element from the end of the array.

3. During each iteration, update `maxi` to store the maximum value among `maxi`, `prefix`, and `suffix`.

4. After the loop, `maxi` will contain the maximum product of any contiguous subarray within `nums`.

5. Return the value of `maxi` as the final result.

This approach efficiently calculates the maximum product by considering products from both the start and end of the array, ensuring that it handles negative numbers and zero values correctly.
'''