class Automation:
    def __init__(self):
        self.state = self._state_Q1

    def _state_Q1(self, arg):
        if arg == "1":
            self.state = self._state_Q2
    
    def _state_Q2(self, arg):
        if arg == "0":
            self.state = self._state_Q3

    def _state_Q3(self, arg):
        self.state = self._state_Q2

    def read_commands(self, commands):
        for command in commands:
            self.state(command)

        return self.state == self._state_Q2


if __name__ == '__main__':
    commands = input()
    print(Automation().read_commands(commands))

