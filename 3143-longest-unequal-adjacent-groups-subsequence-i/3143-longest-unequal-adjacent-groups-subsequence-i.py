class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        indexs = []
        for i in range(len(groups)):
            if indexs and groups[indexs[-1]]==groups[i]:continue
            indexs.append(i)
        res = []
        for index in indexs:
            res.append(words[index])
        return res