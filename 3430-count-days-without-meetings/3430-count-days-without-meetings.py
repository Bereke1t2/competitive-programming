class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        count = 0
        meetings.sort()
        start , end= meetings[0]
        count += start -1
        for curr_start , curr_end in meetings[1:]:
            count += max(curr_start - end -1,0)
            end = max(end,curr_end)
        count +=max(days - end , 0)
        return count

