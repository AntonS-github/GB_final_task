from Models.PackAnimalsABS import PackAnimalsABS


class Horses(PackAnimalsABS):
    '''Класс лошади'''

    def __init__(self, name, birth_date, command):
        super().__init__(name, birth_date, command)

    def eat(self):
        """лошадь умеет есть"""
        pass

    def speak(self):
        """лошадь умеет подавать голос"""
        pass

    def print_animal(self):
        """Распечатать свойства животного"""
        print(f'лошадь: кличка - {self.get_name()}, '
              f'дата рождения - {self.get_birth_date()}, '
              f'команды - {self.get_command()}')