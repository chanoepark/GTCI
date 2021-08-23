"""
LC 102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

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


def levelOrder(root):
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
        
        result.append(currLevel)
    
    return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(f'Level order traversal: {str(levelOrder(root))}')

