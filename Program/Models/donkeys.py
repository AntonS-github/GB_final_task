from Program.Models.PackAnimalsABS import PackAnimalsABS


class Donkeys(PackAnimalsABS):
    '''Класс ослы'''

    def __init__(self, name, birth_date, command):
        super().__init__(name, birth_date, command)

    def eat(self):
        """осёл умеет есть"""
        pass

    def speak(self):
        """осёл умеет подавать голос"""
        pass

    def print_animal(self):
        """Распечатать свойства животного"""
        print(f'осёл: кличка - {self.get_name()}, '
              f'дата рождения - {self.get_birth_date()}, '
              f'команды - {self.get_command()}')