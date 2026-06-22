class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dum = Counter("balloon")
        count = Counter(text)
        return min([count[l]//dum[l] for l in 'balon'])