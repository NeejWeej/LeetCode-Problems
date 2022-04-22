class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # print(stack, 6 // 132)
            if token == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif token == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif token == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
            elif token == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                ans = abs(num2) // abs(num1)
                if num2 < 0:
                    ans *= -1
                if num1 < 0:
                    ans *= -1
                stack.append(ans)
            else:
                stack.append(int(token))
        return stack[0]