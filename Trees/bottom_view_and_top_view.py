from typing import List
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return str(self.__dict__)

def bottomView(root: BinaryTreeNode) -> List[int]:
    if root==None:
        return []
    dist_dict = {0:root.data}
    queue = [(root,0)]

    while queue:
        node, dist = queue.pop(0)

        dist_dict[dist] = node.data

        if node.left:
            queue.append((node.left, dist-1))

        if node.right:
            queue.append((node.right, dist+1))
    
    return [v[1] for v in sorted(dist_dict.items())]

def topView(root):
    if root==None:
        return []
    dist_dict = {0:root.data}
    queue = [(root,0)]

    while queue:
        node, dist = queue.pop(0)

        if dist_dict.get(dist)==None:
            dist_dict[dist] = node.data

        if node.left:
            queue.append((node.left, dist-1))

        if node.right:
            queue.append((node.right, dist+1))
    
    return [v[1] for v in sorted(dist_dict.items())]
    

    


myTree = BinaryTreeNode(1)
myTree.left = BinaryTreeNode(2)
myTree.left.left = BinaryTreeNode(4)
myTree.left.right = BinaryTreeNode(5)

myTree.right = BinaryTreeNode(3)
myTree.right.left = BinaryTreeNode(6)
myTree.right.right = BinaryTreeNode(7)

print(bottomView(myTree))
print(topView(myTree))




'''
Problem1 : https://www.codingninjas.com/studio/problems/bottom-view-of-binary-tree_893110
Problem2 : https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1
TC : O(n)
SC : O(n)
Approach :

**Bottom View:**

1. Initialize an empty dictionary `dist_dict` to store the last seen node at each horizontal distance.
2. Initialize a queue, starting with the root node and a horizontal distance of 0: `queue = [(root, 0)]`.
3. While the queue is not empty:
   - Dequeue a node and its horizontal distance from the front of the queue.
   - Update `dist_dict` with the current node's value at the current horizontal distance.
   - If the current node has a left child, enqueue it with a horizontal distance that is one less.
   - If the current node has a right child, enqueue it with a horizontal distance that is one more.
4. After processing all nodes, return the values of `dist_dict` sorted by their keys (horizontal distances).

**Top View:**

1. Initialize an empty dictionary `dist_dict` to store the first seen node at each horizontal distance.
2. Initialize a queue, starting with the root node and a horizontal distance of 0: `queue = [(root, 0)]`.
3. While the queue is not empty:
   - Dequeue a node and its horizontal distance from the front of the queue.
   - If the current horizontal distance is not in `dist_dict`, add the current node's value to `dist_dict` at that distance.
   - If the current node has a left child, enqueue it with a horizontal distance that is one less.
   - If the current node has a right child, enqueue it with a horizontal distance that is one more.
4. After processing all nodes, return the values of `dist_dict` sorted by their keys (horizontal distances).

'''