def is_valid_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
            print(stack+[0])
        elif char == ')':
            if not stack:
                return False
            stack.pop()
            print(stack+[1])
    return len(stack) == 0

# テスト
print(is_valid_parentheses(")()"))      # True
# print(is_valid_parentheses("(())"))    # True
# print(is_valid_parentheses(")("))     # False
# print(is_valid_parentheses("())"))     # False