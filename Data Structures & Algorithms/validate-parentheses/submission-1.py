class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        dih = { ')': '(', ']': '[', '}': '{' }

        #loop through string
        for char in s:

            #check if a closed parenthesis and correct bracket in top stack
            if char in dih:
                if not stack or stack[-1] != dih[char]:
                    return False
                stack.pop()
            else:
                #push the open parenthesis to stack
                stack.append(char)

        return not stack