# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def init(self,node):
        if node.right:
            node.right.val = 2*node.val +2
            self.init(node.right)
        if node.left:
            node.left.val = 2*node.val + 1
            self.init(node.left)
    def __init__(self, root: Optional[TreeNode]):
        if root:
            root.val = 0    
        self.root = root
        self.init(root)
        
    def isThere(self,root, target):
        if not root:
            return False
        if root.val==target:
            return True
        return self.isThere(root.left,target) or self.isThere(root.right,target)
        
        
    def find(self, target: int) -> bool:
        return self.isThere(self.root , target)
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)