class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = Counter(s1)
        counter2 = defaultdict(int)
        left = 0
        for right in range(len(s2)):
            counter2[s2[right]] +=1
            if right - left+1==len(s1):
                if counter1==counter2:
                    return True
                counter2[s2[left]] -=1
                if not counter2[s2[left]]:del counter2[s2[left]]
                left +=1
        return False