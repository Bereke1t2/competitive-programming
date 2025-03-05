class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0 for i in range(length)]
        stack = []
        for index , temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                i = stack.pop()
                ans[i] =  index-i
            stack.append(index)
        return ans

        