class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        right, left = len(nums) - 1, 0
        
        while left < right:

            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:

                left = mid + 1

            else:

                right = mid

        return nums[left]



        