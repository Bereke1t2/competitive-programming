class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        Sum = sum(apple)
        count = 0
        for length , num in enumerate(sorted(capacity , reverse=True)):
            count += num
            if count>=Sum:
                return length +1
        return -1

