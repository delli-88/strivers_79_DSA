def graphColoring(graph, k, V):
    node_colors = [-1 for _ in range(V)]
    return graphColoringHelper(graph, k, V, 0, node_colors)


def graphColoringHelper(graph, k, V, node, node_colors):

    if node==V:
        return True
    
    for color in range(k):
        if can_we_color(graph, node, color, node_colors):
            node_colors[node] = color
            if graphColoringHelper(graph, k, V, node+1, node_colors):
                return True
            node_colors[node] = -1
    return False


def can_we_color(graph, node, to_color, node_colors):
    v = len(graph[0])
    for i in range(v):
        if graph[node][i]==1 and node_colors[i]==to_color:
            return False
    return True
    
print(graphColoring([[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]],3,4))
'''
Problem : https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1
TC : O(k^V)
SC : O(V)
Approach :

1. Define a `graphColoringHelper` function that takes the graph, the number of colors (`k`), the total number of nodes (`V`), the current node, and an array `node_colors` to store the color assigned to each node.

2. If the current node equals `V`, it means all nodes are colored, so return `True` to indicate a valid coloring.

3. Iterate through each color from 0 to `k-1`.

4. For each color, check if it's safe to assign that color to the current node using the `can_we_color` function.

5. If it's safe, assign the color to the current node in `node_colors`.

6. Recursively call `graphColoringHelper` for the next node (node+1).

7. If the recursion returns `True`, propagate the `True` value up the call stack to indicate a valid coloring.

8. If the recursion returns `False`, backtrack by setting the color of the current node to -1 in `node_colors`.

9. If no valid coloring is found after trying all colors, return `False`.

The `can_we_color` function checks if it's safe to color the current node with a specific color by examining its adjacent nodes.

'''