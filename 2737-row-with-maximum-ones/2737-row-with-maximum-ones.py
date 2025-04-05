class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [-1,-1]
        for index, row in enumerate(mat):
            count = sum(row)
            if count>ans[-1]:
                ans = [index , count]
        return ans