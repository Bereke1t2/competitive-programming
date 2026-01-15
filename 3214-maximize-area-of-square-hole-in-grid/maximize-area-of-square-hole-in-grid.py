class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        count =  2
        max_v = 2
        hBars.sort()
        vBars.sort()
        for index in range(1 , len(hBars)):
            if hBars[index -1]==hBars[index]-1:
                count +=1
            else:
                count = 2
            max_v = max(max_v , count)
        count , max_h = 2 , 2
        for index in range(1 , len(vBars)):
            if vBars[index] == vBars[index -1]+1:
                count +=1
            else:
                count = 2
            max_h = max(count  , max_h)
        return min(max_h , max_v)**2
