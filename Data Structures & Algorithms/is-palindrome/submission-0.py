class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = ""
        for char in s:
            char = char.lower()
            if char.isalnum():
                cleaned += char

        return cleaned == cleaned[::-1]


            

        