class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        N = len(nums)
        for i in range(N-1):
            if nums[i]>nums[i+1]:
                if i == 0 or nums[i-1] <= nums[i+1]:
                    count +=1
                elif i +2 >= N or nums[i+2] >= nums[i]:
                    count +=1
                else:
                    return False
        return count <= 1
