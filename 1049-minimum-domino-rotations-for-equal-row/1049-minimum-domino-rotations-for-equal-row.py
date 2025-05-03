class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for i in range(1 , 7):
            count_top = 0
            count_bot = 0
            for j in range(len(tops)):
                if tops[j]!=i and bottoms[j]!=i:
                    break
                count_top += tops[j]!=i
                count_bot += bottoms[j]!=i
            else:
                return min(count_top , count_bot)
        return -1