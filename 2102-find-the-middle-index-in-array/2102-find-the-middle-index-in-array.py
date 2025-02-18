class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        check = [0]
        for i in range(len(nums)-1,0,-1):
            check.append(check[-1]+nums[i])
        check.reverse()
        Sum = 0 
        for index, num in enumerate(check):
            if Sum == num:
                return index
            Sum +=nums[index]
        return -1
        