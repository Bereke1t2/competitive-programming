class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        MAX = 10**5 + 1

        # Sieve
        is_prime = [True] * MAX
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(MAX**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, MAX, i):
                    is_prime[j] = False

        primes = [i for i in range(MAX) if is_prime[i]]
        prime_set = set(primes)

        total = 0

        for n in nums:
            # case 1: p^3
            p = round(n ** (1/3))
            if p**3 == n and p in prime_set:
                total += 1 + p + p*p + n
                continue

            # case 2: p * q
            for p in primes:
                if p * p > n:
                    break
                if n % p == 0:
                    q = n // p
                    if q != p and q in prime_set:
                        total += 1 + p + q + n
                    break

        return total
