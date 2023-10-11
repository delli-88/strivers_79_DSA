class BinaryTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def minTime(self, root,start):
        if root==None:
            return 0
        
        parents = {root : None}

        queue = [root]
        bfs_queue = []
        
        while queue:
            queue_front = queue.pop(0)

            if queue_front.data==start:
                bfs_queue.append(queue_front)
            
            if queue_front.left:
                parents[queue_front.left] = queue_front
                queue.append(queue_front.left)
            
            if queue_front.right:
                parents[queue_front.right] = queue_front
                queue.append(queue_front.right)

        time_taken = -1
        vis = {}

        while bfs_queue:
            time_taken+=1

            queue_len = len(bfs_queue)

            for _ in range(queue_len):
                curr_node = bfs_queue.pop(0)
                vis[curr_node] = True

                if curr_node.left and vis.get(curr_node.left)==None:
                    bfs_queue.append(curr_node.left)
                
                if curr_node.right  and vis.get(curr_node.right)==None:
                    bfs_queue.append(curr_node.right)
                
                if parents[curr_node]!=None and vis.get(parents[curr_node])==None:
                    bfs_queue.append(parents[curr_node])
            
        return time_taken
    

myTree = BinaryTreeNode(1)
myTree.left = BinaryTreeNode(2)
myTree.left.left = BinaryTreeNode(4)
myTree.left.right = BinaryTreeNode(5)

myTree.right = BinaryTreeNode(3)
myTree.right.left = BinaryTreeNode(6)
myTree.right.right = BinaryTreeNode(7)


print(Solution().minTime(myTree,3))

'''
Problem : https://www.codingninjas.com/studio/problems/time-to-burn-tree_1469067
TC : O(n)
SC : O(n)
Approach :

1. Initialize a `parents` dictionary to keep track of parent-child relationships in the tree.

2. Create a queue for a breadth-first search (BFS) and add the root to it.

3. While the BFS queue is not empty:
   - Dequeue the front node.
   - If the node's value matches the target `start`, add it to a `bfs_queue`.
   - If the node has left and right children, add them to the queue.
   - Update the `parents` dictionary with the parent-child relationship.

4. Initialize a `time_taken` variable to `-1` and an empty `vis` dictionary to keep track of visited nodes.

5. While the `bfs_queue` is not empty:
   - Increment `time_taken` by 1.
   - Process all nodes at the current level:
     - Mark the current node as visited in the `vis` dictionary.
     - If the left child is unvisited, add it to the `bfs_queue`.
     - If the right child is unvisited, add it to the `bfs_queue`.
     - If the parent node is unvisited, add it to the `bfs_queue`.

6. Return the `time_taken` as the time it takes to burn from the root to the node with value `start`.

'''