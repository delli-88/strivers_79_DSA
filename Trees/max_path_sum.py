from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [-float("inf")]
        self.maxPathSumHelper(root, max_sum)
        return max_sum[0]

    def maxPathSumHelper(self, root, max_sum):
        if root==None:
            return -float("inf")

        left_sum = self.maxPathSumHelper(root.left, max_sum)
        right_sum = self.maxPathSumHelper(root.right, max_sum)

        max_sum[0] = max(max_sum[0], root.val, root.val + left_sum, root.val + right_sum,  root.val + left_sum + right_sum)

        return max(root.val, root.val + left_sum , root.val + right_sum)

'''
Problem : https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
TC : O(n)
SC : O(h)
Approach:

1. We maintain a `max_sum` variable to keep track of the maximum path sum encountered so far. Initialize it with negative infinity to ensure that the first path encountered will be greater.

2. We define a recursive helper function `maxPathSumHelper` that takes a node `root` and `max_sum` as parameters. This function returns the maximum path sum starting from the current node going downwards.

3. In the helper function:
   - If the `root` is `None`, we return 0 because there's no path to contribute.
   - We recursively calculate the maximum path sum in the left subtree and right subtree using `left_sum` and `right_sum`.
   - We update `max_sum` by comparing it with different possibilities:
     - `root.val`: The maximum path sum starting from the current node.
     - `root.val + left_sum`: The maximum path sum including the current node and going left.
     - `root.val + right_sum`: The maximum path sum including the current node and going right.
     - `root.val + left_sum + right_sum`: The maximum path sum that connects left and right subtrees through the current node.
   - Finally, we return the maximum of three values: `root.val`, `root.val + left_sum`, and `root.val + right_sum`. This represents the maximum path sum starting at the current node and going down one side.

4. In the `maxPathSum` function, we call the helper function starting from the root node and update `max_sum` accordingly.

5. After traversing the entire tree, `max_sum[0]` will contain the maximum path sum.

'''