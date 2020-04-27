class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # read in string upto the operator; evaluate two numbers before it
        # append sln to the list in place and keep doing the same until the end
        # use stack to make it easier to pop and add elements

        valid_ops = ['+', '-', '*', '/']

        stack = []

        for op in tokens:
            if op not in valid_ops:
                stack.append(int(op))
            else:
                n1 = stack.pop()
                n2 = stack.pop()

                if op == '+':
                    res = n1 + n2
                elif op == '-':
                    res = n2 - n1
                elif op == '*':
                    res = n2 * n1
                else:
                    res = int(n2 / n1)

                stack.append(res)
               # print(res)
           # print(stack)

        sol = stack.pop()

        return sol
