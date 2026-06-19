class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_ = 0
        curr = 0
        for num in gain:
            curr +=num
            max_ = max(max_ , curr)
        return max_
