class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_ = deque()
        left = 0
        res=[]

        for right in range(len(nums)):
            while max_ and max_[-1]<nums[right]:
                max_.pop()
            max_.append(nums[right])
            if right - left+1==k:
                res.append(max_[0])
                if max_[0]==nums[left]:
                    max_.popleft()
                left +=1
        return res