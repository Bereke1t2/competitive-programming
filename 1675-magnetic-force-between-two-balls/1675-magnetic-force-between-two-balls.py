class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def good(guss):
            nonlocal position , m
            curr= position[0]
            for _ in range(m-1):
                curr +=guss
                index = bisect_left(position,curr)
                if index>=len(position):
                    return False
                curr = position[index]
            return True

        left , right = 1, max(position)
        ans = 0

        while left<=right:
            guss = (left + right)//2
            if good(guss):
                ans = guss
                left = guss +1 
            else:
                right = guss - 1
        return ans