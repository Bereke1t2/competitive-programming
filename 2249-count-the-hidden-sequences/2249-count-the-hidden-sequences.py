class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_  = max_ = num = 0

        for diff in differences:
            num +=diff
            min_ = min(min_ , num)
            max_ = max(max_ , num)
        diff = lower - min_
        check = upper - (max_ + diff)
        return max(0 , check+1)