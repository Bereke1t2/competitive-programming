class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)
        max_ = 0
        for i in range(len(arr)):
            for j in range(i+ 1,len(arr)):
                count = 2
                target = arr[i] + arr[j]
                prev = arr[j]
                while target in s:
                    prev , target = target ,  prev + target
                    print(target)
                    count +=1
                max_ = max(max_ , count)
        return max_ if max_ > 2 else 0

                