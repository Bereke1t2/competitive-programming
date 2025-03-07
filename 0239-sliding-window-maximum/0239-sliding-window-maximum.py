class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()

        left = 0
        for right in range(len(nums)):
            while q and q[-1]<nums[right]:
                q.pop()
            q.append(nums[right])
            if right - left +1>k:
                if q[0]==nums[left]:
                    q.popleft()
                left +=1
            if right - left +1 ==k:
                ans.append(q[0])
        return ans
            


            

        