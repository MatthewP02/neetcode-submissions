class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0

        for operation in operations:
            match operation:
                case "+":
                    new = stack[-2] + stack[-1]
                    stack.append(new)
                    total += new
                case "D":
                    new = stack[-1]*2
                    stack.append(new)
                    total += new
                case "C":
                    total -= stack.pop()
                case _:
                    new = int(operation)
                    stack.append(new)
                    total += new

        return total