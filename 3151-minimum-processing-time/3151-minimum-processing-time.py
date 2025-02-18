class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        n  = len(processorTime)
        max_ = 0
        for i in range(len(processorTime)):
            max_ = max(max_,processorTime[i] + tasks[4*(i+1) - 1])
        return max_


