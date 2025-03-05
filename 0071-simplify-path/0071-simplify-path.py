class Solution:
    def simplifyPath(self, path: str) -> str:
        path = [p for p in path.split('/') if p]
        stack = []
        for p in path:
            if p=='.':continue
            if p == '..':
                if stack:stack.pop()
            else:
                stack.append(p)
        return '/'+'/'.join(stack)
        