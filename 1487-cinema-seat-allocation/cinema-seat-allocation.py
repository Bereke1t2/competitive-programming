class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        block = defaultdict(list)
        for row , seat in reservedSeats:
            block[row].append(seat)
        count = 0
        for row in block.keys():
            first = True 
            last = True
            middle  = True
            for seat in sorted(block[row]):
                if 2<= seat <=5:
                    first = False
                if 4 <= seat <= 7:
                    middle = False
                if 6<= seat <= 9:
                    last = False
            if first and last:
                count +=2
            elif first or last or middle:
                count +=1
        return n*2 - len(block)*2 + count

