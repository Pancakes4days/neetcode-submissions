class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dih = defaultdict(int)
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dih:
                return [dih[complement], i]
            dih[num] += i
        return [-1, -1]
        