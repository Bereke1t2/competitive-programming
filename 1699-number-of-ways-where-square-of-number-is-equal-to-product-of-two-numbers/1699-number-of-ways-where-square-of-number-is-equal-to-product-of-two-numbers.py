class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        d1_ml = defaultdict(int)
        d2_ml = defaultdict(int)

        for i in range(len(nums1)):
            for j in range(i,len(nums1)):
                if i==j:d1_ml[nums1[i]*nums1[j]] +=1
                else:
                    d1[nums1[i]*nums1[j]] +=1
        for i in range(len(nums2)):
            for j in range(i,len(nums2)):
                if i==j:d2_ml[nums2[i]*nums2[j]] +=1
                else:
                    d2[nums2[i]*nums2[j]] +=1
        count = 0
        for key in d1_ml:
            count +=d1_ml[key]*d2[key]
        for key in d2_ml:
            count +=d2_ml[key]*d1[key]
        return count
