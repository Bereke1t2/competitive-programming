class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        make = [0]*(amount+1)
        make[0] = 1
        for coin in coins:
            for num in range(coin , amount +1):
                make[num] += make[num - coin]
        return make[-1]