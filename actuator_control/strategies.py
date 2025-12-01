from actuator_control.base_actuator import ControlStrategy
from common.utils.debug import Debugger
from actuator_control.fan.actuator_fan_digital import FanDigital

debug = Debugger()

class ManualControl(ControlStrategy):
    def __init__(self, connector_manager):
        self.cm = connector_manager

    def apply(self, aktor):
        duty = self.cm.connectors["mode"].get_fan_speed()
        aktor.activate(duty)


class AutoControl(ControlStrategy):
    def __init__(self, temp_connector, threshold_connector):
        self.temp_connector = temp_connector
        self.threshold_connector = threshold_connector


    def apply(self, actuator):
        # Temperatur aus InfluxDB
        current_temp = self.temp_connector.read()
        # Schwellwert aus MariaDB (z.B. Level 1)
        thresholds = self.threshold_connector.read()
        threshold_value = thresholds.get(100)  # Level 1 = Hauptschwellwert

        if current_temp is None or threshold_value is None:
            debug.log("Keine gültigen Daten für AutoControl", label="AutoControl")
            actuator.activate(0)
            return

        if isinstance(actuator, FanDigital):
            # Digital: nur Level 100 relevant
            threshold_value = thresholds.get(100)
            if threshold_value and current_temp >= threshold_value:
                actuator.activate(100)
                debug.log("Fan On", label="Autocontrol")
            else:
                actuator.activate(0)
                debug.log("Fan Off", label="Autocontrol")
        else:
            # PWM: mehrere Stufen
            duty = 0
            for level in sorted(thresholds.keys()):
                if current_temp >= thresholds[level]:
                    duty = level
            actuator.activate(duty)
            debug.log(f"Temp={current_temp} → Duty={duty}", label="AutoControl")

