from abc import ABC, abstractmethod

# Абстрактный класс 'Животные'
class Animals(ABC):
    def __init__(self, name, birthday, command):
        self.name = name
        self.birthday = birthday
        self.command = command

    @abstractmethod
    def print_animal(self):
        pass

