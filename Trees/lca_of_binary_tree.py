class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lowestCommonAncestorHelper(root, p, q)
    
    def lowestCommonAncestorHelper(self, root, p, q):

        if root==None:
            return None
        
        if root.val==p or root.val==q:
            return root
        
        left = self.lowestCommonAncestorHelper(root.left, p, q)
        right = self.lowestCommonAncestorHelper(root.right, p, q)

        if left and right:
            return root
        
        if left:
            return left
        
        if right:
            return right
        
        return None

'''
Problem : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
TC : O(n)
SC : O(h) ~ O(log n)
Approach :

1. We have a binary tree with a root node, and we want to find the LCA of two nodes, `p` and `q`.

2. We define a recursive helper function `lowestCommonAncestorHelper` that takes the current node `root`, and the two nodes `p` and `q` as parameters.

3. In the helper function:
   - If `root` is `None`, we return `None`, as there is no common ancestor.
   - If `root` is equal to either `p` or `q`, we return `root` itself because a node is considered its ancestor.
   - We recursively search for `p` and `q` in the left and right subtrees, storing the results in the `left` and `right` variables.

4. After we have the results from both the left and right subtrees:
   - If both `left` and `right` are not `None`, it means that `p` and `q` are found in both subtrees, and the current `root` is their lowest common ancestor. We return `root` in this case.
   - If only `left` is not `None`, we return `left` as the LCA.
   - If only `right` is not `None`, we return `right` as the LCA.
   - If both `left` and `right` are `None`, we return `None` as there is no common ancestor.

5. In the `lowestCommonAncestor` function, we call the helper function starting from the root node and return the result.

'''