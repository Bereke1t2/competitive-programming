class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = set([l for l in "qwertyuiop"])
        s2 = set([l for l in "asdfghjkl"])
        s3 = set([l for l in "zxcvbnm"])

        res = []

        for word in words:
            temp = word.lower()
            s = set([l for l in temp])
            if s <= s1 or s<=s2 or s<=s3:
                res.append(word)
        return res