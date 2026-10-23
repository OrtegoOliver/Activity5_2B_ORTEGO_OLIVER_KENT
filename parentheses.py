def balanced_parentheses(expression):
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


expression = input("Enter an expression: ")

if balanced_parentheses(expression):
    print("The parentheses are balanced.")
else:
    print("The parentheses are not balanced.")