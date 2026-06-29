class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(l in word for l in patterns)