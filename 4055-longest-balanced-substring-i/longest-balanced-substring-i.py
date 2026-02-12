class Solution:
    def longestBalanced(self, s: str) -> int:
        for length in range(len(s) , 1 , -1):
            left = 0
            count = Counter()
            for right in range(len(s)):
                count[s[right]] +=1
                if right - left +1== length:
                    if len(set(count.values()))==1:
                        return length
                    count[s[left]] -=1
                    if not count[s[left]]: del count[s[left]]
                    left +=1
        return 1