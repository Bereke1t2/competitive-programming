class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        left = 0
        d= defaultdict(int)

        for right in range(len(s)):
            d[s[right]] +=1
            while len(d)==3:
                count += len(s)-right
                d[s[left]] -=1
                if not d[s[left]]:
                    del d[s[left]]
                left +=1
        return count
            


        