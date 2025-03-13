# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count  = 0
        def paths(root , prefix_sum , d , traget_sum):
            if not d[0]:
                d[0] = 1
            if not root:
                return
            nonlocal count
            prefix_sum +=root.val
            count +=d[prefix_sum-traget_sum]
            d[prefix_sum] +=1
            
            paths(root.left , prefix_sum , d , traget_sum)
            paths(root.right , prefix_sum , d , traget_sum)

            d[prefix_sum] -=1
            prefix_sum -=root.val
        paths(root,0 , defaultdict(int) , targetSum)
        return count


