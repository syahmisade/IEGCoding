'''
Write a Python class to check the validity of a string of parentheses,
'(', ')', '{', '}', '[' and '].
These brackets must be closed in the correct order, for example
"()" and "()[]{}" are valid
"[)", "({[)]" and "{{{" are invalid.
'''


class ParenthesesValidator:
    def __init__(self):
        self.pair_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

    def is_valid(self, s: str):
        stack = []
        for char in s:
            if char in self.pair_map.values():
                stack.append(char)
            elif char in self.pair_map.keys():
                if stack == [] or self.pair_map[char] != stack.pop():  # Check if the closing Parthss is correct
                    return False
            else:
                # Invalid character encountered
                return False
        return True


# Example usage
validator = ParenthesesValidator()
print(validator.is_valid("()"))       # True
print(validator.is_valid("()[]{}"))   # True
print(validator.is_valid("(]"))       # False
print(validator.is_valid("({[)]"))    # False
print(validator.is_valid("{{{"))      # False
