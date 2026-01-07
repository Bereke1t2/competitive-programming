class StringHash:
    def __init__(self, s):
        self.s = s
        self.n = len(s)

        # two large primes
        self.mod1 = 10**9 + 7
        self.mod2 = 10**9 + 9

        # fixed base (important for CP)
        self.base = 911382323

        self.h1 = [0] * (self.n + 1)
        self.h2 = [0] * (self.n + 1)
        self.p1 = [1] * (self.n + 1)
        self.p2 = [1] * (self.n + 1)

        for i in range(self.n):
            c = ord(s[i])  # use raw ascii for safety
            self.h1[i + 1] = (self.h1[i] * self.base + c) % self.mod1
            self.h2[i + 1] = (self.h2[i] * self.base + c) % self.mod2
            self.p1[i + 1] = (self.p1[i] * self.base) % self.mod1
            self.p2[i + 1] = (self.p2[i] * self.base) % self.mod2

    def get_hash(self, l, r):
        """ returns hash of s[l..r] inclusive """
        x1 = (self.h1[r + 1] - self.h1[l] * self.p1[r - l + 1]) % self.mod1
        x2 = (self.h2[r + 1] - self.h2[l] * self.p2[r - l + 1]) % self.mod2
        return (x1, x2)



class Solution:
    def longestDupSubstring(self, s: str) -> str:
        h = StringHash(s)
        def poss(length):
            nonlocal h
            seen = set()
            left = 0
            for right in range(length-1 , len(s)):
                if right - left +1 == length:
                    sub_s = h.get_hash(left , right)
                    if sub_s in seen:
                        return (left , right)
                    seen.add(sub_s)
                    left +=1
            return (-1 , -1 )
        left , right = 0 , len(s) - 1
        ans = (left , right)
        while left <= right:
            mid = (left + right)//2
            res = poss(mid)
            if res != (-1 , -1):
                ans = res
                left = mid + 1
            else:
                right = mid -1
        return s[ans[0]:ans[1]+1]


