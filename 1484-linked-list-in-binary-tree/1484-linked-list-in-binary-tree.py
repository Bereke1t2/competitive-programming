class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        targetPath = []
        while head:
            targetPath.append(head.val)
            head = head.next
        
        def compare(left, right):
            return "".join(map(str, right)) in "".join(map(str, left))

        currPath = []
        verdict = False
        def dfs(node):
            nonlocal verdict
            if not node: return
            currPath.append(node.val)
            if not node.left and not node.right:
                if compare(currPath, targetPath):
                    verdict = True
                return
            if node.left:
                dfs(node.left)
                currPath.pop()
            if node.right:
                dfs(node.right)
                currPath.pop()

        dfs(root)
        return verdict