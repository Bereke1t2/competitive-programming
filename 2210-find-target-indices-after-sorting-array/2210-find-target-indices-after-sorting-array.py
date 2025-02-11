class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = bisect_left(nums,target)
        right = bisect_right(nums,target)
        res = []
        for i in range(right-left):
            res.append(left)
            left +=1
        return res