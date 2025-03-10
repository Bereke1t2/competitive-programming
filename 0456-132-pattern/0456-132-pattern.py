class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        miin = nums[0]
        for num in nums[1:]:
            while stack and stack[-1][0]<=num:
                stack.pop()
            if stack and num>stack[-1][1]:
                return True
            stack.append((num,miin))
            miin = min(miin,num)
        return False
