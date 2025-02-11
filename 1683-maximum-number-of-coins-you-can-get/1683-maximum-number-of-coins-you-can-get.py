class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        count  = 0
        index = len(piles)-2
        length = len(piles)//3
        piles.sort()
        while length>0:
            count += piles[index]
            index -=2
            length -=1
        return count
        