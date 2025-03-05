class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1]*len(nums1)
        for index , num in enumerate(nums1):
            i = nums2.index(num)
            print(index,i)
            for j in range(i+1,len(nums2)):
                if nums2[j]>num:
                    print(nums2[j],">",num)
                    ans[index] = nums2[j]
                    break
        return ans