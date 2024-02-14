"""
A = ["2", "1", "+", "3", "*"]
Algorithm:
1. Evaluate for each character in postfix expression
2. If operand is encountered, push into stack
3. If operator is encountered, pop 2 characters from stack
which were already filled in stack.
first = top element stack
second = second element from stack
4. Check for operator & push into stack after operation
second operator first
5. return top element from stack.
"""


def eval_expression(arr):
    stack = []
    operator = ["+", "-", "*", "/", "%"]

    for item in arr:
        if item not in operator:
            stack.append((item))
        else:
            first = int(stack.pop())
            sec = int(stack.pop())

            if item == "+":
                stack.append(sec + first)

            if item == "-":
                stack.append(sec - first)

            if item == "*":
                stack.append(sec * first)

            if item == "/":
                stack.append(sec / first)

            if item == "%":
                stack.append(sec % first)

    return stack[-1]


A = ['5', '1', '2', '/', '4', '*', '+', '3', '-']
print(eval_expression(A))



