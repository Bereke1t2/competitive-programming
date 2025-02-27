class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        odd = [0]
        even =[0]
        odd_sum = even_sum = 0
        for i in range(len(nums)):
            if i%2:
                odd_sum +=nums[i]
            else:
                even_sum +=nums[i]
            odd.append(odd_sum)
            even.append(even_sum)
        count = 0
        for i in range(len(odd)-1):
            if even[i] +odd[-1] - odd[i+1] == odd[i] + even[-1] - even[i+1]:
                count +=1
        return count
        
        