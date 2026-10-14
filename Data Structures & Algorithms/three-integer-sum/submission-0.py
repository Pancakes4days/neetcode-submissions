class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        l, r = 0, len(nums) - 1
        triplets = []

        for i in range(len(nums) - 2):
            
            l, r = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            while l < r:

                third = -nums[i]
                if nums[l] + nums[r] < third:            
                    l += 1
                elif nums[l] + nums[r] > third:
                    r -= 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return triplets







        