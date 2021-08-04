from commands import CommandInterface
from typing import Type

class Button:

    def __init__(self) -> None:
        self.__command = None

    def set_command(self, command: Type[CommandInterface]) -> None:
        self.__command = command
    
    def action(self) -> None:
        if self.__command:
            self.__command.execute()

