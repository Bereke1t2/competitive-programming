class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums =  SortedList()
        res = [num1 - num2 for num1 , num2 in zip(nums1 , nums2)]
        count = 0
        for i in range(len(nums1) -1 , -1 ,-1):
            count +=(len(nums) -  bisect_left(nums , res[i]-diff))
            nums.add(res[i])
        return count