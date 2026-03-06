class Solution(object):
    def calculate(self, s):
        stack = []
        res = 0
        num = 0
        sign = 1  # 1 for '+', -1 for '-'
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                res += sign * num
                num = 0
                sign = 1
            elif char == '-':
                res += sign * num
                num = 0
                sign = -1
            elif char == '(':
                # Save the result and sign before the parenthesis
                stack.append(res)
                stack.append(sign)
                # Reset for the new sub-expression
                res = 0
                sign = 1
            elif char == ')':
                res += sign * num
                num = 0
                # Combine with the sign and result before '('
                res *= stack.pop() # This was the sign
                res += stack.pop() # This was the previous result
        
        return res + (sign * num)