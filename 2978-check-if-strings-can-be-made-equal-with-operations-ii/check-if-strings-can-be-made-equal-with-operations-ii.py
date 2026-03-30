from collections import Counter

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1 = Counter([ch for i, ch in enumerate(s1) if i % 2 == 0])
        odd1  = Counter([ch for i, ch in enumerate(s1) if i % 2 == 1])

        even2 = Counter([ch for i, ch in enumerate(s2) if i % 2 == 0])
        odd2  = Counter([ch for i, ch in enumerate(s2) if i % 2 == 1])

        return even1 == even2 and odd1 == odd2