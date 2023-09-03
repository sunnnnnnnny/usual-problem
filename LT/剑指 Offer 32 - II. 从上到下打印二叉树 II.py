# https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/
"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。



例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        result = []
        if root is None:
            return result
        result.append([root.val])
        queue = [root]
        while queue:
            queue_temp = []
            result_temp = []
            while len(queue) > 0:
                node = queue.pop(0)
                print(node.val)
                if node.left is not None:
                    queue_temp.append(node.left)
                    result_temp.append(node.left.val)
                if node.right is not None:
                    queue_temp.append(node.right)
                    result_temp.append(node.right.val)
            if len(result_temp) >0:
                result.append(result_temp[:])
            queue = queue_temp
        return result