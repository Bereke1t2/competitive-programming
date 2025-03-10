class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        curr_sum = 0
        count =0
        for right in range(len(arr)):
            curr_sum +=arr[right]
            if right - left + 1==k:
                count +=curr_sum/k>=threshold
                curr_sum -=arr[left]
                left +=1
        return count
