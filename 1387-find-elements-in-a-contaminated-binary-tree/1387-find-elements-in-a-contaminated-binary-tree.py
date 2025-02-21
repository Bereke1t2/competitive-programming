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
            self.store.add(node.right.val)
            self.init(node.right)
        if node.left:
            node.left.val = 2*node.val + 1
            self.store.add(node.left.val)
            self.init(node.left)
    def __init__(self, root: Optional[TreeNode]):
        self.store = set()
        if root:
            root.val = 0
            self.store.add(0)    
        self.root = root
        self.init(root)   
        
    def find(self, target: int) -> bool:
        return target in self.store
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)