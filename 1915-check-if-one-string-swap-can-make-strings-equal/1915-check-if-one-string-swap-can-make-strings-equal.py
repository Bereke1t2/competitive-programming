class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        change = defaultdict(int)
        for l1 , l2 in zip(s1,s2):
            if l1 != l2:
                if l1 in change:
                    return False
                change[l1] = l2
                check = l1
        if len(change)==2:
            return  change[change[check]] == check
        return len(change)==0

