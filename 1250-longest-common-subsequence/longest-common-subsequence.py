class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = defaultdict(int)
        n1 , n2 = len(text1) , len(text2)
        def dp(i , j):
            nonlocal memo
            if i>=n1 or j >=n2:
                return 0
            if (i , j) in memo:
                return memo[(i,j)]
            if text1[i]==text2[j]:
                ans = 1 + dp(i+1 , j +1)
            else:
                ans = max(dp(i+1 , j) , dp(i , j+1))
            memo[(i,j)] = ans
            return ans
        return dp(0 , 0)