class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        p1 = p2 = 0
        heap =  [(nums1[p1] + nums2[p2] , p1 , p2)]
        seen = set()
        while heap:
            ans , p1 , p2 = heappop(heap)
            res.append([nums1[p1] , nums2[p2]])
            p1 +=1
            if p1<len(nums1) and p2<len(nums2) and (p1, p2 ) not in seen:
                heappush(heap , (nums1[p1] + nums2[p2] , p1 , p2))
                seen.add((p1 , p2))
            p2 +=1
            p1 -=1
            if p1<len(nums1) and p2<len(nums2) and (p1, p2 ) not in seen:
                heappush(heap , (nums1[p1] + nums2[p2] , p1 , p2))
                seen.add((p1 , p2))
            if len(res)==k:
                return res
