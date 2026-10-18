class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        
        for cha in tokens:
            if cha in ops:
                b = stack[-1]
                stack.pop()
                a = stack[-1]
                match cha:
                    case '+':
                        stack[-1] = a + b
                    case '-':
                        stack[-1] = a - b
                    case '*':
                        stack[-1] = a * b
                    case _:
                        stack[-1] = int(a / b)
            else:
                stack.append(int(cha))

        return int(stack[-1])
