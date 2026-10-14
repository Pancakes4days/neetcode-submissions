class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            result[key].append(strs[i])

        return list(result.values())