class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = right = 0
        t_freq = Counter(t)
        s_freq = Counter()
        l , r = 0, len(s)
        Min = 2*len(s)
        if len(s)==1:
            return s if s==t else ""
        def check(t1,t2):
            return not t1 - t2
        while right < len(s):
            s_freq[s[right]] +=1
            while left <= right and check(t_freq, s_freq):
                if Min>right - left +1:
                    Min = right - left +1
                    l , r =left , right
                s_freq[s[left]] -=1
                left +=1
            right +=1
        return s[l:r+1] if Min != 2*len(s) else ""

            
            
