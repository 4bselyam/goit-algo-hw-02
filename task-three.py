def check_brackets(expression):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack:
                return "Несиметрично"
            elif stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return "Несиметрично"

    return "Симетрично" if not stack else "Несиметрично"
