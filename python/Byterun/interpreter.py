from collections import deque


class Interpreter:
    def __init__(self):
        self.stack = deque()

    def PUSH_VALUE(self, value):
        self.stack.append(value)

    def ADD_TWO_NUMBERS(self):
        n1 = self.stack.pop()
        n2 = self.stack.pop()
        self.stack.append(n1+n2)

    def PRINT_ANSWER(self):
        print(self.stack.pop())

    def run_it(self, what_to_run):
        instructions = what_to_run['instructions']
        values = what_to_run["values"]
        for instruction in instructions:
            op, arg = instruction
            if op == "PUSH_VALUE":
                self.PUSH_VALUE(values[arg])
            elif op == "PRINT_ANSWER":
                self.PRINT_ANSWER()
            else:
                self.ADD_TWO_NUMBERS()
