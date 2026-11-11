class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
            }



        for tok in tokens:

            if tok in operations:

                b = stack.pop()
                a = stack.pop()

                added = operations[tok](a,b)
                stack.append(added)

            else:
                stack.append(int(tok))

        return stack[0]





