from typing import List
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        min_bananas = float("inf")
        
        while start<=end:
            mid = (start+end)//2
            time_taken = self.timeTaken(piles, mid)

            if time_taken<=h:
                min_bananas = mid
                end = mid-1
            else:
                start = mid+1

        return min_bananas

    def timeTaken(self, piles, speed):
        time = 0
        for i in range(len(piles)):
            time += ceil(piles[i]/speed)
        return time

print(Solution().minEatingSpeed(piles = [30,11,23,4,20], h = 6))


'''
Problem : https://leetcode.com/problems/koko-eating-bananas/description/
TC : O(n log(max(arr)))
SC : O(1)
Approach :
1. Initialize two pointers, `start` and `end`, to represent the search range for the eating speed. Set `start` to 1 (minimum possible speed) and `end` to the maximum number of bananas in any pile (maximum possible speed).

2. Initialize a variable `min_bananas` to positive infinity (`float("inf")`). This variable will keep track of the minimum eating speed that allows you to finish eating all the bananas in `h` hours.

3. Use a `while` loop to perform binary search within the search range:
   - Calculate the middle value `mid` as `(start + end) // 2`.

   - Calculate the time required to eat all the bananas at the current eating speed using the `timeTaken` function.

   - Compare `time_taken` with `h` (available time):
     - If `time_taken` is less than or equal to `h`, it means you can eat all the bananas in `h` hours at the current eating speed. In this case, update `min_bananas` to `mid` (the current eating speed) and move the search range to the left by setting `end` to `mid - 1`.

     - If `time_taken` is greater than `h`, it means you need more time to eat all the bananas at the current eating speed. In this case, move the search range to the right by setting `start` to `mid + 1`.

4. After the `while` loop completes, return the value of `min_bananas`, which represents the minimum eating speed required to eat all the bananas in `h` hours.

'''