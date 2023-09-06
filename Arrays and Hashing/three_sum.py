from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        for firstEle in range(len(nums)-2):
            if firstEle!=0 and nums[firstEle]==nums[firstEle-1]:
                continue
            start = firstEle + 1
            end = len(nums) - 1
            while start<end:
                currSum = nums[firstEle] + nums[start] + nums[end]
                if currSum > 0:
                    end-=1
                elif currSum < 0:
                    start+=1
                else:
                    sol.append([nums[firstEle], nums[start], nums[end]])
                    start+=1
                    end-=1
                    while start<end and nums[start]==nums[start-1]:
                        start+=1
                    while start<end and nums[end]==nums[end+1]:
                        end-=1
        return sol
    
print(Solution().threeSum(nums = [-2,0,1,1,2]))

'''
Problem : https://leetcode.com/problems/3sum/description/
TC - O(n^2)
SC - O(1)

Approach:

1. Sort the input list `nums` in non-decreasing order to simplify the process.

2. Initialize an empty list `sol` to store triplet solutions.

3. Iterate through the sorted list, considering each element as a potential first element (`firstEle`) of a triplet.

4. To avoid duplicate triplets, skip elements with the same value as the previous one (except for the first element).

5. Use a two-pointer approach with `start` and `end` pointers to find pairs of elements in the remaining list that sum to the negation of `firstEle`.

6. Adjust the pointers based on the current sum (`currSum`):
   - If `currSum` is greater than zero, decrement `end`.
   - If `currSum` is less than zero, increment `start`.
   - If `currSum` is zero, append `[firstEle, nums[start], nums[end]]` to `sol`, and increment `start` while decrementing `end` to find other valid triplets with the same `firstEle`. Skip duplicate values for `start` and `end`.

7. Return the `sol` list, which contains all unique triplets that sum to zero.

'''