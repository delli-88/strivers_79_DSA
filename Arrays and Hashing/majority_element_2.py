from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority_one_count = 0
        majority_two_count = 0
        majority_one_ele = None
        majority_two_ele = None

        for i in range(len(nums)):
            if majority_one_count==0 and majority_two_ele!=nums[i]:
                majority_one_count+=1
                majority_one_ele = nums[i]
            elif majority_two_count==0 and majority_one_ele!=nums[i]:
                majority_two_count+=1
                majority_two_ele = nums[i]
            elif nums[i]==majority_one_ele:
                majority_one_count+=1
            elif nums[i]==majority_two_ele:
                majority_two_count+=1
            else:
                majority_one_count-=1
                majority_two_count-=1
        
        final_majority_one_count = 0
        final_majority_two_count = 0

        for i in range(len(nums)):
            if nums[i]==majority_one_ele:
                final_majority_one_count+=1
            elif nums[i]==majority_two_ele:
                final_majority_two_count+=1
        majority = []
        if final_majority_one_count>len(nums)//3:
            majority.append(majority_one_ele)
        if final_majority_two_count>len(nums)//3:
            majority.append(majority_two_ele)
        
        return majority


print(Solution().majorityElement(nums = [1,1,1,1,2,2,2,2,3,3,3,3]))

'''
Problem : https://leetcode.com/problems/majority-element-ii/ 
TC : O(n)
SC : O(1)
Approach :
1. Initialize `majority_one_count`, `majority_two_count`, `majority_one_ele`, and `majority_two_ele` to manage two potential majority elements.

2. Iterate through the `nums` list:
   - If `majority_one_count` is 0 and the current element is not equal to `majority_two_ele`, set `majority_one_count` to 1 and assign the current element to `majority_one_ele`.
   - Else if `majority_two_count` is 0 and the current element is not equal to `majority_one_ele`, set `majority_two_count` to 1 and assign the current element to `majority_two_ele`.
   - Else if the current element is equal to `majority_one_ele`, increment `majority_one_count`.
   - Else if the current element is equal to `majority_two_ele`, increment `majority_two_count`.
   - Otherwise, decrement both `majority_one_count` and `majority_two_count`.

3. Count the occurrences of `majority_one_ele` and `majority_two_ele` in the `nums` list and store them in `final_majority_one_count` and `final_majority_two_count`.

4. Initialize an empty list `majority` to store the majority elements.

5. If `final_majority_one_count` is greater than ⌊ n/3 ⌋, add `majority_one_ele` to the `majority` list.

6. If `final_majority_two_count` is greater than ⌊ n/3 ⌋, add `majority_two_ele` to the `majority` list.

7. Return the `majority` list containing the majority elements.

'''
