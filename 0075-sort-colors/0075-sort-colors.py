class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0]*3
        for num in nums:
            count[num] +=1
        j = 0
        for i in range(3):
            while count[i]:
                nums[j] = i
                j +=1
                count[i] -=1
        return nums
        