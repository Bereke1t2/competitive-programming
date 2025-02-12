class Solution:
    def sortSentence(self, s: str) -> str:
        words = ['']*9
        for word in s.split(' '):
            words[int(word[-1])-1] = word[:-1]
        return ' '.join(words).rstrip()
        