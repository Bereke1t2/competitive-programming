class Solution:
    def nthUglyNumber(self, n: int) -> int:

        def count_ugly(x):
            count = 0

            def dfs(value, start):
                nonlocal count

                if value > x:
                    return

                count += 1

                for factor in (2, 3, 5):
                    if factor >= start:
                        dfs(value * factor, factor)

            dfs(1, 2)
            return count

        left, right = 1, 2_000_000_000_000

        while left < right:
            mid = (left + right) // 2

            if count_ugly(mid) >= n:
                right = mid
            else:
                left = mid + 1

        return left