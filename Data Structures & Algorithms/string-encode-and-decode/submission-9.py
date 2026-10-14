class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""
        for word in strs:
                encoded_string += str(len(word)) + "#" + word
        return encoded_string

    def decode(self, s: str) -> List[str]:

        result = []
        left = 0
        while left < len(s):
            right = left
            while s[right] != '#':
                right += 1
            length = int(s[left:right])
            word = s[right + 1 : right + 1 + length]
            result.append(word)
            left = right + 1 + length
        return result
           
