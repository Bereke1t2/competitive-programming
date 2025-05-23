class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        frq = Counter(tasks)
        count = 0
        for val in frq.values():
            last = val
            temp = val 
            while temp>=0:
                if temp%2==0:
                    last = temp
                temp -=3
            count += ((val - last)//(3) + (last//2))
            if (val - last)%3!=0 or last%2!=0:
                return -1
        return count
