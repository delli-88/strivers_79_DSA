from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = [0]
        self.diameterOfBinaryTreeHelper(root, max_diam)
        return max_diam[0]
    
    def diameterOfBinaryTreeHelper(self, root, max_diam):
        if root ==None:
            return 0

        left_height = self.diameterOfBinaryTreeHelper(root.left, max_diam)
        right_height = self.diameterOfBinaryTreeHelper(root.right, max_diam)

        max_diam[0] = max(max_diam[0], left_height+right_height)

        return 1 + max(left_height, right_height)

'''
Problem : https://leetcode.com/problems/diameter-of-binary-tree/
TC : O(n)
SC : O(h)
Approach :

1. We use a helper function `diameterOfBinaryTreeHelper` to calculate the height of the binary tree rooted at the current node.

2. In the `diameterOfBinaryTreeHelper` function, we first check if the current node is `None`. If it is, we return 0, indicating that the height of the subtree rooted at this node is 0.

3. We then recursively calculate the heights of the left and right subtrees by calling `diameterOfBinaryTreeHelper` on the left and right children of the current node.

4. We update the `max_diam` list with the maximum diameter found so far. The diameter of the tree rooted at the current node is equal to the sum of the heights of its left and right subtrees.

5. We return the height of the current subtree, which is the maximum of the heights of its left and right subtrees plus 1 (to account for the current node).

6. Finally, in the `diameterOfBinaryTree` function, we initialize `max_diam` as a list containing a single element with an initial value of 0. We call the helper function to calculate the diameter of the entire binary tree rooted at `root` and return the value stored in `max_diam[0]`, which represents the diameter of the tree.
'''
    


