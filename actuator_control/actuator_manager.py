from actuator_control.strategies import ManualControl, AutoControl
from data_connector.temperature_connector import TemperatureConnector
from data_connector.threshold_connector import ThresholdConnector
from actuator_control.socket.actuator_socket_tapop100 import SocketTAPOp100
from actuator_control.fan.actuator_fan_digital import FanDigital
from actuator_control.fan.actuator_fan_pwm import FanPWM

class ActuatorManager:
    def __init__(self, actuators, connector_manager):
        self.actuators = actuators
        self.cm = connector_manager
        # Connectoren für AutoControl
        temp_connector = TemperatureConnector()
        threshold_connector = ThresholdConnector()

        self.strategies = {
            'manual': ManualControl(connector_manager),
            'auto': AutoControl(temp_connector, threshold_connector)
        }

    def run(self):
        mode = self.cm.get("mode")  # z. B. 'manual' oder 'auto'
        strategy = self.strategies.get(mode, self.strategies['manual'])

        for actuator in self.actuators:
            if isinstance(actuator, FanPWM) or isinstance(actuator, FanDigital):
                strategy.apply(actuator)
            elif isinstance(actuator, SocketTAPOp100):
                actuator.activate()

            