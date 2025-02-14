class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = max_val = 0
        tracker = defaultdict(int)
        for right in range(len(fruits)):
            tracker[fruits[right]] +=1
            while len(tracker)>2:
                tracker[fruits[left]] -=1
                if not tracker[fruits[left]]:
                    del tracker[fruits[left]]
                left +=1
            max_val = max(max_val,sum(tracker.values()))
        return max_val