class StringHash:
    def __init__(self, s: str):
        self.s = s
        self.n = len(s)
        self.base = 31
        self.mod = 1_000_000_009
        self.prefix_hash = [0] * (self.n + 1)
        self.power = [1] * (self.n + 1)
        for i in range(1, self.n + 1):
            self.prefix_hash[i] = (self.prefix_hash[i - 1] * self.base + ord(s[i - 1])) % self.mod
            self.power[i] = (self.power[i - 1] * self.base) % self.mod

    def get_hash(self, l: int, r: int) -> int:
        return (self.prefix_hash[r + 1] - self.prefix_hash[l] * self.power[r - l + 1]) % self.mod


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return ''
        forward = StringHash(s)
        back = StringHash(s[::-1])
        n = len(s)
        max_ = 1
        for i in range(n):
            if forward.get_hash(0 , i) == back.get_hash(n-i-1 , n-1):
                max_ = i +1
        return s[max_:][::-1] + s
        