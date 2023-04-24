from abc import abstractmethod

from Models.Animals_ABS import Animals


class PetsABS(Animals):
    """Абстрактный класс Вьючные животные"""

    @abstractmethod
    def eat(self):
        """Животное умеет есть"""
        pass

    @abstractmethod
    def speak(self):
        """Животное умеет подавать голос"""
        pass
