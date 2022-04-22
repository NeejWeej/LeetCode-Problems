class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if (len(token) > 1 and token[0] == '-') or token.isnumeric():
                stack.append(int(token))
                continue
            num1 = stack.pop()
            num2 = stack.pop()
            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num2 - num1)
            elif token == '*':
                stack.append(num1 * num2)
            elif token == '/':
                ans = abs(num2) // abs(num1)
                if num2 < 0:
                    ans *= -1
                if num1 < 0:
                    ans *= -1
                stack.append(ans)
        return stack[0]