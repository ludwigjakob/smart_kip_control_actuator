# interfaces.py
from abc import ABC, abstractmethod

class Actuator(ABC):
    @abstractmethod
    def set_duty_cycle(self, value: int): pass

class ControlStrategy(ABC):
    @abstractmethod
    def apply(self, aktor: Actuator): pass