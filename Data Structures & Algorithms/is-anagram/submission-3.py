class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        template = defaultdict(int)
        duplicate = defaultdict(int)

        for char in s:
            template[char] += 1

        for char in t:
            duplicate[char] += 1

        return template == duplicate

        