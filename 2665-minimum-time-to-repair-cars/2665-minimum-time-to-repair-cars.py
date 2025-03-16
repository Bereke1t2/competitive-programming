class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        n = len(ranks)
        def check(mint):
            nonlocal ranks , cars
            c = cars
            for r in ranks:
                c -= int((mint/r)**0.5)
            return c<1

        min_t = float('inf')
        left , right = 0 , max(ranks)*(cars//n +1)**2
        while left <= right :
            mid = (left + right)//2
            if check(mid):
                right = mid -1
            else:
                left = mid +1
        return left
        