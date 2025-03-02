class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        p1, p2 = 0, 0 
        
        while p1 < len(nums1) and p2 < len(nums2):
            first_0, first_1 = nums1[p1][0], nums1[p1][1]
            second_0, second_1 = nums2[p2][0], nums2[p2][1]
            
            if first_0 == second_0:
                res.append([first_0, first_1 + second_1])
                p1 += 1
                p2 += 1
            elif first_0 < second_0:
                res.append([first_0, first_1])
                p1 += 1
            else:
                res.append([second_0, second_1])
                p2 += 1
        
        while p1 < len(nums1) or p2 < len(nums2):
            if p1 < len(nums1):
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1
        
        return res