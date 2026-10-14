class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        checks = defaultdict(int)
        checkt = defaultdict(int)
        
        for char in s:
            checks[char] += 1
        for char in t:
            checkt[char] += 1

        return checks == checkt

        