class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_letters = [0]*26
        t_letters = [0]*26
        for i in range(len(s)):
            s_letters[ord(s[i])-ord('a')] +=1
            t_letters[ord(t[i])-ord('a')] +=1
        diff_elment = 0
        for i in range(26):
            diff_elment += abs(s_letters[i] - t_letters[i])
        return diff_elment//2
        
