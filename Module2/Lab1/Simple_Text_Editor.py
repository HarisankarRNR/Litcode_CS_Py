import sys
class CustomStack:
    def __init__(self):
        self.text = ""
        self.commands = []

    def insert(self, value):
        self.text += value

    def delete(self, value):
        if len(self.text) > value:
            self.text = self.text[:-value]

    def get(self, value):
        return self.text[value-1]

    def undo(self):
        if self.commands:
            command = self.commands.pop()
            if command[0] == '1':
                self.delete(len(command[1]))
            elif command[0] == '2':
                self.insert(command[1])
            elif command[0] == '3':
                self.insert(command[1])
            elif command[0] == '4':
                self.undo()

    def execute_command(self, command):
        command_parts = command.split(' ')
        command_type = command_parts[0]

        if command_type == '1':
            value = command_parts[1]
            self.insert(value)
        elif command_type == '2':
            value = int(command_parts[1])
            self.delete(value)
        elif command_type == '3':
            value = int(command_parts[1])
            result = self.get(value)
            if result:
                print(result)
        elif command_type == '4':
            self.undo()

        self.commands.append(command_parts)


# Exercise-1
editor = CustomStack()
commands_str = input()
commands=commands_str.split(',')
for command in commands:
    editor.execute_command(command)
                                                                                                                            