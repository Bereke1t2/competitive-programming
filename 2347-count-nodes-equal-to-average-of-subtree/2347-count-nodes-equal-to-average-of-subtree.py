# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0

        def dfs(root):
            nonlocal count
            if not root:
                return [0 , 0]
            
            left_count  , left_sum = dfs(root.left)
            right_count , right_sum = dfs(root.right)

            total_count = left_count + right_count +1
            total_sum = left_sum + right_sum + root.val

            if total_sum//total_count == root.val:
                count +=1
            return total_count , total_sum

        dfs(root)
        return count
        


