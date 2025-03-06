def is_valid(s: str) -> bool:
    parentheses_map = {"}": "{", "]": "[", ")": "("}
    stack = []
    for char in s:
        if char in parentheses_map.values():
            stack.append(char)
        elif char in parentheses_map.keys():
            if not stack:
                return False
            last_char = stack.pop()
            if not last_char == parentheses_map[char]:
                return False
    return not len(stack)


test_cases = [
    ("(]", False),
    ("([])", True),
    ("()[]{}(({{}})){{}}{[]}{[][]}", True),
    ("()", True),
    ("[", False),
    ("]", False),
]

for s, expected_output in test_cases:
    output = is_valid(s)
    assert output == expected_output, f"{s}"
