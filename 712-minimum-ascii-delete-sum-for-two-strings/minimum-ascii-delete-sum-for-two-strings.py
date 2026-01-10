class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = defaultdict(int)
        l1 , l2 = len(s1) , len(s2)

        def dp(i , j):
            if i>=l1 or j >= l2:
                return 0
            if (i , j) in memo:
                return memo[(i,j)]
            if s1[i]==s2[j]:
                ans =  2*ord(s1[i]) + dp(i+1 , j+1)
            else:
                ans = max(dp(i+1 , j) , dp(i , j+1))
            memo[(i , j)] = ans
            return ans
        return sum(ord(c) for c in s1) + sum(ord(c) for c in s2) - dp(0 , 0)
