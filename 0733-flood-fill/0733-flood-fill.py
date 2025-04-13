class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions_straight = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows , cols = len(image) , len(image[0])
        def is_inbound(x, y):
            return 0 <= x < rows and 0 <= y < cols

        colored = set()
        def dfs(par_color ,i ,j):
            if (i,j) in colored or not is_inbound(i , j ) or par_color != image[i][j]:
                return

            image[i][j] = color
            colored.add((i,j))
            for incx , incy in directions_straight:
                dfs(par_color , i + incx , j +incy)
        
        dfs(image[sr][sc] , sr,sc)
        return image