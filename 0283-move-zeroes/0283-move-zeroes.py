class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        holder = -1
        for i in range(len(nums)):
            if nums[i]==0:
                holder = i
                break

        if holder == -1:
            return nums

        for s in range(holder+1,len(nums)):
            if nums[holder]==0 and nums[s]!=0:
                nums[holder],nums[s] = nums[s],nums[holder]
                holder+=1
        return nums