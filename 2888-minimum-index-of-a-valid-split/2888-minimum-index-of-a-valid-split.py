class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        d = Counter(nums)
        max_ =0
        num = 0
        for key in d:
            if max_<d[key]:
                num = key
                max_ =d[key]
        for i in range(len(nums)-1):
            curr = nums[i]
            d[nums[i]] -=1
            if curr == num:
                if 2*(max_ - d[nums[i]]) > i + 1 and 2*d[nums[i]]> len(nums) - i -1:
                    return i
        return -1
