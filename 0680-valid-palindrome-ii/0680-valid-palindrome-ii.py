class Solution:
    def validPalindrome(self, s: str) -> bool:
        left , right = 0, len(s)-1
        count = 0
        while left<right:
            if s[left]!=s[right]:
                remove_left  = s[right:left:-1] == s[left+1:right+1]
                remove_right = s[left:right][::-1] == s[left:right]
                if remove_left or remove_right:
                    break
                return False
            right -=1
            left +=1
        return True
            
        