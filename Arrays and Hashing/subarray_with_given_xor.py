class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        freq_dict = {0:1}
        num_subarrays = 0
        xor_till_now = 0
        for i in range(len(A)):
            xor_till_now = xor_till_now ^ A[i]
            front_xor = xor_till_now ^ B
            if freq_dict.get(front_xor):
                num_subarrays+= freq_dict[front_xor]
            freq_dict[xor_till_now] = freq_dict.get(xor_till_now, 0)+1
        return num_subarrays


print(Solution().solve( A = [4, 2, 2, 6, 4], B = 6))

'''
Problem : https://www.interviewbit.com/problems/subarray-with-given-xor/
TC : O(n)
SC : O(n)
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

'''