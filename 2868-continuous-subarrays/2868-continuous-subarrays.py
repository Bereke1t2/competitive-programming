class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        min_ = deque()
        max_ = deque()

        left = count = 0
        for right in range(len(nums)):
            num = nums[right]
            while min_ and min_[-1]>num:
                min_.pop()
            min_.append(num)
            while max_ and max_[-1]<num:
                max_.pop()
            max_.append(num)

            while max_[0]-min_[0]>2 and left < right:
                num = nums[left]
                if max_[0]==num:
                    max_.popleft()
                if min_[0]==num:
                    min_.popleft()
                left +=1
            count +=(right - left +1)
        return count

