from abc import ABC, abstractmethod


# Абстрактный класс 'Животные'
class Animals(ABC):
    def __init__(self, name, birthday, command):
        self.name = name
        self.birthday = birthday
        self.command = command

    def get_name(self) -> str:
        return self.name

    def get_birth_date(self) -> str:
        return self.birthday

    def get_command(self) -> str:
        return self.command

    @abstractmethod
    def print_animal(self):
        pass
