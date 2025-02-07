class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        f_word2 = {}
        res = []
        for word in words2:
            for l , cnt in dict(Counter(word)).items():
                f_word2[l] = max(f_word2.get(l,0),cnt)
        for word1 in words1:
            f_word1 = dict(Counter(word1))
            flage = False
            for l, cnt in f_word2.items():
                if f_word1.get(l,0) < cnt:
                    flage = not flage
                    break
            if not flage:
                res.append(word1)
        return res

        