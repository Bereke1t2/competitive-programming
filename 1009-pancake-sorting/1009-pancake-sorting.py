class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        length = len(arr)
        for i in range(len(arr),0,-1):
            k = arr.index(i)
            if k:
                res.append(k+1)
            arr = arr[k::-1] + arr[k+1:]
            arr = arr[length-1::-1]
            res.append(length)
            length -=1
        return res
