class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        miin = float("inf")
        nums.sort()
        for i in range(len(nums)-2):
            curr_target = target - nums[i]
            left , right = i+1 , len(nums)-1
            while left < right:
                curr_sum = nums[left]+nums[right] 
                if curr_sum ==curr_target:
                    miin = target
                    break
                elif curr_sum<curr_target:
                    left +=1
                elif curr_sum>curr_target:
                    right -=1
                if abs(curr_target-curr_sum)<abs(target-miin):
                    miin = curr_sum + nums[i]
        return miin

            
        