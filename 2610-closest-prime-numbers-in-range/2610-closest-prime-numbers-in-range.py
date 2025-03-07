class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n):
            sieve = [True] * (n + 1)
            sieve[0] = sieve[1] = False
            for i in range(2, int(math.sqrt(n)) + 1):
                if sieve[i]:
                    for j in range(i*i, n+1, i):
                        sieve[j] = False
            return [i for i, is_prime in enumerate(sieve) if is_prime]
        nums = sieve(right)
        ans = [-1,-1]
        min_ = right - left +1
        for i in range(1,len(nums)):
            if nums[i-1]>=left and min_> nums[i]-nums[i-1]:
                min_ = nums[i]- nums[i-1]
                ans = [nums[i-1] , nums[i]]
        return ans