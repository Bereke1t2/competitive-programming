class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def can_assign(k: int) -> bool:
            tasks_k = tasks[:k]
            workers_k = workers[-k:]
            avail = workers_k.copy()
            cur_pills = pills

            for need in reversed(tasks_k):
                if avail[-1] >= need:
                    avail.pop()
                else:
                    if cur_pills == 0:
                        return False
                    target = need - strength
                    idx = bisect.bisect_left(avail, target)
                    if idx == len(avail):
                        return False
                    avail.pop(idx)
                    cur_pills -= 1
            return True

        lo, hi = 0, min(len(tasks), len(workers))
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_assign(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans