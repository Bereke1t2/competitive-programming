class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        for i in range(len(nums2)):
            d[nums2[i]] = -1
            while stack and nums2[stack[-1]]<nums2[i]:
                d[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        return [d[i] for i in nums1]