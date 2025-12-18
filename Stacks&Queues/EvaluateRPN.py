class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/" :
                stack.append(int(token))
                continue
            
            number_2 = stack.pop()
            number_1 = stack.pop()

            if token == "+":
                num = number_2 + number_1
            elif token == "-":
                num = number_1 - number_2
            elif token == "*":
                num = number_1 * number_2
            else:
                num = int (number_1 / number_2)

            stack.append(num)
        
        return stack.pop()
