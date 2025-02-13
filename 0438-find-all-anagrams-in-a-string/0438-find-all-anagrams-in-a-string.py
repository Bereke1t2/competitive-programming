class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        check = defaultdict(int)
        left = right = 0
        res = []
        while right<len(s):
            if right - left ==len(p):
                if check==counter:
                    res.append(left)
                check[s[left]] -=1
                if check[s[left]]==0:
                    del check[s[left]]
                left +=1
            check[s[right]] +=1
            right +=1
        if check==counter:
            res.append(left)
        return res