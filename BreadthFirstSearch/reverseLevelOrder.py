"""
LC 107. Binary Tree Level Order Traversal II

Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. 
(i.e., from left to right, level by level from leaf to root).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def reverseLevelOrder(root):
    # Same as levelOrder but reversed result
    if not root:
        return []
    
    result = []
    queue = []
    queue.append(root)

    while queue:
        levelSize = len(queue)
        currLevel  = []

        for _ in range(levelSize):
            currNode = queue.pop(0)
            currLevel.append(currNode.val)
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
        
        result.insert(0, currLevel)
    
    return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(f'Reverse level order traversal: {str(reverseLevelOrder(root))}')

