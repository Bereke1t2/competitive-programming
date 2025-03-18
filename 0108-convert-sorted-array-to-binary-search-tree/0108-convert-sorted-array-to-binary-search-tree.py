# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        head = TreeNode(nums[len(nums)//2])

        def make(root , node):
            if not root:
                return node
            if  root.val  == node.val:
                return root
            if root.val  > node.val:
                root.left = make(root.left, node)
            else:
                root.right = make(root.right , node)
            
            return root
        
        def do(s , e):
            nonlocal head
            if s== e:
                head = make(head , TreeNode(nums[s]))
                return
            if s>e:
                return 
            head = make(head , TreeNode(nums[ceil((s+e)/2)]))
            do(s , ceil((s+e)/2) -1 )
            do(ceil((s+e)/2) + 1 , e)
        do(0 , len(nums)-1)
        return head