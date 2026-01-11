class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights):
            stack =[]
            max_area = 0

            for index , height in enumerate(heights):
                start = index
                if len(stack)!=0:
                    while stack and stack[-1][1]> height:
                        last_index , last_height = stack.pop()
                        start = last_index
                        max_area = max(max_area,last_height* (index-last_index))
                stack.append((start,height))
            for index , height in stack:
                max_area= max(max_area, height*(len(heights)-index))
            return max_area
        max_area = 0
        heights = [0 for i in range(len(matrix[0]))]
        for row in matrix:
            for index , num in enumerate(row):
                if num == "1":
                    heights[index] += 1
                else:
                    heights[index] = 0
            max_area = max(max_area,largestRectangleArea(heights))
        return max_area
                    



