class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        malt_map = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                malt_map[nums[i]*nums[j]] +=1
        cal = lambda num:(num-1)*(num)//2
        count = 0

        for key in malt_map:
            count +=(cal(malt_map[key])*8)

        return count
