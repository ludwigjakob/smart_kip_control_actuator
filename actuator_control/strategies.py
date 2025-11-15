from actuator_control.base_actuator import ControlStrategy
from debug import Debugger

debug = Debugger()

class ManualControl(ControlStrategy):
    def __init__(self, connector_manager):
        self.cm = connector_manager

    def apply(self, aktor):
        duty = self.cm.connectors["mode"].get_fan_speed()
        aktor.set_duty_cycle(duty)


class AutoControl(ControlStrategy):
    def __init__(self):
        pass

    def apply(self, aktor):
        debug.log("[AUTO MODE]", label="AutoControl")
        aktor.set_duty_cycle(0)
