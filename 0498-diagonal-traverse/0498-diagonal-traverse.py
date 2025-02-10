class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        res = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                d[row + col].append(mat[row][col])
        for key , nums in d.items():
            if not key%2:
                nums.reverse()
            res.extend(nums)
        return res
