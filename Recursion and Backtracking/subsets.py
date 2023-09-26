from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subsetHelper(0, nums, [], [])

    def subsetHelper(self, pos, inp, out, sol):
        if pos==len(inp):
            sol.append(out[:])
            return sol

        self.subsetHelper(pos+1, inp, out, sol)

        out.append(inp[pos])
        self.subsetHelper(pos+1, inp, out, sol)
        out.pop()

        return sol

print(Solution().subsets(nums = [1,2,3]))


'''
Problem : 
TC : O(2^n)
SC : O(n)
Approach :

1. Initialize an empty list `sol` to store the subsets.
2. Define a recursive helper function `subsetHelper` that takes four parameters:
   - `pos`: the current position in the input `nums`.
   - `inp`: the input list.
   - `out`: the current subset being constructed.
   - `sol`: the list of all subsets.
3. In the `subsetHelper` function:
   - If `pos` is equal to the length of `inp`, it means we have reached the end of the input list. In this case, we append a copy of the `out` list to `sol` to store the subset.
   - Recursively call `subsetHelper` with the next position (`pos+1`) without including the current element in `out`.
   - Add the current element `inp[pos]` to the `out` list, then recursively call `subsetHelper` with the next position (`pos+1`) with the current element included.
   - After the recursive calls, remove the last element from the `out` list to backtrack.
4. Start the recursion by calling `subsetHelper(0, nums, [], [])`.
5. Return the `sol` list containing all the generated subsets.

'''
