class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        transposed = [list(row[::-1]) for row in list(zip(*matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] = transposed[row][col]        