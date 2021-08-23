"""
LC 103. Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

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


def zigZagLevelOrder(root):
    if not root:
        return []
    
    queue = [root]
    result = []
    level = 0

    while queue:
        levelSize = len(queue)
        currLevel = []

        for _ in range(levelSize):
            currNode = queue.pop(0)
            if level % 2:
                currLevel.insert(0, currNode.val)
            else:
                currLevel.append(currNode.val)
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
        
        level += 1
        result.append(currLevel)
    
    return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(f'Level order traversal: {str(zigZagLevelOrder(root))}')

