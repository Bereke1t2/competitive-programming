class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = [ [-1]*len(nums) for _ in range(len(nums))]
        def game(left , right):
            if left==right:
                return nums[left]
            if left>right:
                return 0
            if memo[left][right]!=-1:
                return memo[left][right]

            take_left =  nums[left] - game(left + 1 , right)
            take_right = nums[right] - game(left , right -1)
            memo[left][right] = max(take_left , take_right)
            
            return memo[left][right]
        return game(0,len(nums)-1)>=0