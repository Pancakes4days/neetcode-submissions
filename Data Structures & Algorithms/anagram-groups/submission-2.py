class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

            anagrams = defaultdict(list)

            for string in strs:

                characters = sorted(string)
                anagram = "".join(characters)
                anagrams[anagram].append(string)

            return list(anagrams.values())