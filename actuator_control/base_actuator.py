# interfaces.py
from abc import ABC, abstractmethod

class Actuator(ABC):
    @abstractmethod
    def activate(self, value: int): pass

    @abstractmethod
    def stop(self, value: int): pass


class ControlStrategy(ABC):
    @abstractmethod
    def apply(self, aktor: Actuator): pass