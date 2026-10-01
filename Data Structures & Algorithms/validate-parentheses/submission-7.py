class Solution:
    def isValid(self, s: str) -> bool:
        opened = []
        matches = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for letter in s:
            if letter in matches.keys():
                if not opened or opened and opened.pop() != matches[letter]:
                    return False
            else:
                opened.append(letter)

        return True if not opened else False