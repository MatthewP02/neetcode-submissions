class Solution:
    def __init__(self):
        self.stack = []

    def operate(self, operation):
        if operation == "+":
            temp = self.stack.pop()
            new = self.stack[-1] + temp
            self.stack.append(temp)
            self.stack.append(new)
        elif operation == "C":
            self.stack.pop()
        elif operation == "D":
            self.stack.append(self.stack[-1]*2)
        else:
            self.stack.append(int(operation))


    def ssum(self):
        total = 0
        while self.stack:
            total += self.stack.pop()

        return total

    def calPoints(self, operations: List[str]) -> int:
        for operation in operations:
            self.operate(operation)

        total = self.ssum()
        return total