from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.combinationSumHelper(0, candidates, [], [], 0, target)
    
    def combinationSumHelper(self, pos, inp, out, sol, comb_sum, target):
        
        if comb_sum==target or pos==len(inp):
            if comb_sum==target:
                sol.append(out[:])
            return sol
        
        out.append(inp[pos])
        self.combinationSumHelper(pos, inp, out, sol, comb_sum+inp[pos], target)
        out.pop()

        self.combinationSumHelper(pos+1, inp, out, sol, comb_sum, target)

        return sol

print(Solution().combinationSum(candidates = [2,3,6,7], target = 7))

'''
Problem:
TC : O(2^target * k)
SC : O(n)
Approach :

1. Define a recursive helper function `combinationSumHelper` that takes six parameters:
   - `pos`: the current position in the `inp` list.
   - `inp`: the input list containing candidate numbers.
   - `out`: the current combination being constructed.
   - `sol`: the list of all valid combinations.
   - `comb_sum`: the current sum of elements in the `out` combination.
   - `target`: the target sum we want to achieve.
2. In the `combinationSumHelper` function:
   - If `comb_sum` is greater than or equal to `target` or `pos` has reached the end of `inp`, the function checks if `comb_sum` is equal to `target`. If it is, it appends a copy of the `out` combination to `sol` since it's a valid combination.
   - The function then proceeds to the next step regardless of whether the sum condition is met.
   - Add the current element `inp[pos]` to the `out` combination and recursively call `combinationSumHelper` with the same parameters, but with `pos` and `comb_sum` updated accordingly.
   - After the recursive call, remove the last element from the `out` combination to backtrack.
   - Recursively call `combinationSumHelper` with `pos+1` (moving to the next element in `inp`) and without changing the current `out` and `comb_sum` values.
3. Start the recursion by calling `combinationSumHelper(0, inp, [], [], 0, target)`.
4. Return the `sol` list containing all valid combinations.

'''