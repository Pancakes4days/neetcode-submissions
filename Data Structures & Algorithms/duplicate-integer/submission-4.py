class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        validity = False
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                validity = True
            else:
                seen.add(nums[i])
        return validity