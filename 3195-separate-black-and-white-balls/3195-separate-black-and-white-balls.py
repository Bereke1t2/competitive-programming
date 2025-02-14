class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        left = right = 0
        for right in range(len(s)):
            if s[right] == '0':
                count +=right -left
                left +=1
        return count
        