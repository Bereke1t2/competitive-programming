class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
          left = 0
          right = len(nums)-1
          resulte = [-1,-1]
          while left<=right:
            mid = (left+right)//2

            if  nums[mid]>=target:
                if nums[mid]==target:
                    resulte[0]=mid
                right = mid -1
            else:
                left = mid+1
        
          left = 0
          right = len(nums)-1
          while left<=right:
            mid = (left+right)//2
            if  nums[mid]<=target:
                if nums[mid]==target:
                    resulte[1]=mid
                left = mid + 1
            else:
                right = mid-1
            

          return resulte


            

                
