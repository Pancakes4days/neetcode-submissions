class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #arrange them by number and frequency of it showing up
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        #add the k biggest into solution
        ordered = sorted(d.items(), key=lambda kv: -kv[1])
        return [num for num, freq in ordered[:k]]

            

        